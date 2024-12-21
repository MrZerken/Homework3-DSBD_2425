import grpc
from concurrent import futures
import time
import os

from dsbd_pb2_grpc import DSBDServiceServicer, add_DSBDServiceServicer_to_server
from command_handler import CommandHandler
from query_handler import QueryHandler

# Import Prometheus
from prometheus_client import start_http_server, Counter, Gauge
import time as pytime

# Leggiamo il nome del nodo per le metriche
node_name = os.environ.get("NODE_NAME", "unknown_node")
service_name = "dsbd_grpc_server"

# Definizione metriche Prometheus
# COUNTER per il numero di chiamate RPC effettuate
rpc_requests_total = Counter('grpc_rpc_requests_total', 
                             'Total number of RPC requests received',
                             ['service', 'node', 'rpc_method'])

# GAUGE per la latenza dell’ultima chiamata RPC
rpc_latency_seconds = Gauge('grpc_rpc_request_latency_seconds',
                            'Latency of the last RPC request in seconds',
                            ['service', 'node', 'rpc_method'])

# Avvio del server Prometheus su una porta dedicata (8000)
start_http_server(8000)


class DSBDServer(DSBDServiceServicer):
    def __init__(self):
        self.command_handler = CommandHandler()
        self.query_handler = QueryHandler()
    
    def _measure_rpc(self, rpc_name, func, request):
        """
        Wrapper per misurare la latenza e incrementare il contatore
        delle chiamate RPC.
        """
        rpc_requests_total.labels(service=service_name, node=node_name, rpc_method=rpc_name).inc()
        start_time = pytime.time()
        response = func(request)
        latency = pytime.time() - start_time
        rpc_latency_seconds.labels(service=service_name, node=node_name, rpc_method=rpc_name).set(latency)
        return response

    def LoginUser(self, request, context):
        return self._measure_rpc("LoginUser", self.command_handler.LoginUser, request)

    def RegisterUser(self, request, context):
        return self._measure_rpc("RegisterUser", self.command_handler.RegisterUser, request)

    def UpdateUser(self, request, context):
        return self._measure_rpc("UpdateUser", self.command_handler.UpdateUser, request)

    def UpdateUserThresholds(self, request, context):
        return self._measure_rpc("UpdateUserThresholds", self.command_handler.UpdateUserThresholds, request)

    def ResetUserThresholds(self, request, context):
        return self._measure_rpc("ResetUserThresholds", self.command_handler.ResetUserThresholds, request)

    def DeleteUser(self, request, context):
        return self._measure_rpc("DeleteUser", self.command_handler.DeleteUser, request)

    def GetTickerValue(self, request, context):
        return self._measure_rpc("GetTickerValue", self.query_handler.GetTickerValue, request)

    def GetTickerAverage(self, request, context):
        return self._measure_rpc("GetTickerAverage", self.query_handler.GetTickerAverage, request)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DSBDServiceServicer_to_server(DSBDServer(), server)
    server.add_insecure_port('[::]:18072')
    server.start()
    print("Il server è in esecuzione sulla porta 18072...")
    try:
        while True:
            time.sleep(86400)  # Mantiene il server attivo
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
