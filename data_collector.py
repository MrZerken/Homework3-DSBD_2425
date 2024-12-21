import threading
import time
import yfinance as yf
import pytz
from database import SessionLocal, User, StockData
from datetime import datetime
from confluent_kafka import Producer
import json
import os

# Prometheus imports
from prometheus_client import start_http_server, Gauge, Counter

# Leggo il nome del nodo per le label delle metriche
node_name = os.environ.get("NODE_NAME", "unknown_node")

# Nome del servizio (per le label)
service_name = "data_collector"

# Definizione metriche Prometheus
# COUNTER: Numero totale di aggiornamenti richiesti
update_requests_total = Counter('data_collector_update_requests_total', 
                                'Number of total update_data requests', 
                                ['service', 'node'])

# GAUGE: Latenza dell'operazione di aggiornamento dati
update_latency_seconds = Gauge('data_collector_update_latency_seconds', 
                               'Latency of update_data operation in seconds', 
                               ['service', 'node'])

# Avvio del server Prometheus su una porta dedicata (es. 8000)
start_http_server(8000)


# Configurazione Kafka per produttore
producer_config = {
    'bootstrap.servers': 'kafka-service:9092',
    'acks': 'all',
    'batch.size': 500,
    'max.in.flight.requests.per.connection': 1,
    'retries': 3
}

producer = Producer(producer_config)
topic1 = 'to-alert-system'

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

class CircuitBreaker:
    def __init__(self, max_failures=5, reset_time=20, exception=Exception):
        self.max_failures = max_failures
        self.reset_time = reset_time
        self.exception = exception
        self.nFailures = 0
        self.state = 'CLOSED'
        self.last_failure_time = None
        self.lock = threading.Lock()

    def fetch_stock_values(self, tickers):
        values = {}
        for ticker in tickers:
            try:
                data = yf.Ticker(ticker)
                last_price = data.fast_info['lastPrice']
                values[ticker] = last_price
            except Exception as e:
                print(f"Errore durante il recupero del ticker {ticker}: {e}")
                values[ticker] = None
        return values

    def update_stock_data(self):
        session = SessionLocal()
        users = session.query(User).all()
        tickers = set(user.ticker for user in users)

        with self.lock:
            if self.state == 'OPEN':
                time_since_failure = time.time() - self.last_failure_time
                if time_since_failure > self.reset_time:
                    self.state = 'HALF_OPEN'
                else:
                    raise CircuitBreakerOpenException("Circuito aperto, chiamata negata.")

            # Incremento del contatore di richieste di aggiornamento
            update_requests_total.labels(service=service_name, node=node_name).inc()

            start_time = time.time()
            try:
                ticker_values = self.fetch_stock_values(tickers)
            except self.exception as e:
                self.nFailures += 1
                self.last_failure_time = time.time()
                if self.nFailures >= self.max_failures:
                    self.state = 'OPEN'
                raise e

            if self.state == 'HALF_OPEN':
                self.state = 'CLOSED'
                self.nFailures = 0

            for user in users:
                value = ticker_values.get(user.ticker)
                if value is not None:
                    stock_data = StockData(
                        user_id=user.id,
                        ticker=user.ticker,
                        value=value,
                        timestamp=datetime.now()
                    )
                    session.add(stock_data)
                    print(f"Aggiornato il dato di {user.email} per {user.ticker}: {value}")
                else:
                    print(f"Nessun dato disponibile per {user.ticker}.")

            session.commit()
            session.close()

            # Calcolo della latenza e aggiornamento del GAUGE
            latency = time.time() - start_time
            update_latency_seconds.labels(service=service_name, node=node_name).set(latency)

            # Notifica Kafka
            message = {'message': 'Aggiornamento dei dati azionari completato con successo.'}
            producer.produce(topic1, json.dumps(message), callback=delivery_report)
            producer.flush()


circuit_breaker = CircuitBreaker()


class CircuitBreakerOpenException(Exception):
    pass


def stock_market_open():
    # Verifica se il mercato è aperto (EU, Rome).
    time_zone = pytz.timezone('Europe/Rome')
    current_time = datetime.now(time_zone)
    if current_time.weekday() >= 5:
        return False
    # Orari di apertura del mercato (9:30 - 16:00)
    market_open = current_time.replace(hour=9, minute=30, second=0, microsecond=0)
    market_close = current_time.replace(hour=16, minute=0, second=0, microsecond=0)
    return market_open <= current_time <= market_close


if __name__ == '__main__':
    while True:
        if True: #FIXME reimpostare a stock_market_open()
            try:
                circuit_breaker.update_stock_data()
            except CircuitBreakerOpenException as e:
                print(e)
        else:
            print("Mercato Azionario chiuso. Nessun Aggiornamento Eseguito.")
        time.sleep(120)

