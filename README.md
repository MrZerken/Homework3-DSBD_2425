# Guida alla Build e Deploy

## *Bonafede Salvatore Luca* - *Bontempo Gaetano*

## Configurazione di Minikube

### Avvia Minikube
```bash
minikube start
```

### Crea un Namespace
```bash
kubectl create namespace dsbd-namespace
```

### Configurazione dell’Ambiente Docker
Per targhettare `docker-env` e costruire le immagini all'interno di Minikube:
```bash
minikube docker-env | Invoke-Expression
```

### Build delle Immagini Docker
Esegui i seguenti comandi per costruire le immagini dei container personalizzati:
```bash
docker build -t grpc-server:latest -f server/Dockerfile.server .
docker build -t data-collector:latest -f data_collector/Dockerfile.datacollector .
docker build -t cp_alertsystem:latest -f alertSystem/Dockerfile.cp_alertsystem .
docker build -t c_alertnotifiersystem:latest -f alertSystem/Dockerfile.c_alertnotifiersystem .
```

### Caricamento dei Manifests Kubernetes
Carica i manifest nella namespace:
```bash
kubectl apply -f ./manifests/ -n dsbd-namespace
```

### Verifica dello Stato dei Pods
Controlla lo stato dei pods e attendi che siano tutti in stato `Running` prima di procedere:
```bash
kubectl get pods -n dsbd-namespace
```

### Esporre il GRPC Server
Per esporre la porta del server e utilizzarlo con il client:
```bash
kubectl port-forward svc/grpc-server 18072:18072 -n dsbd-namespace
```

---

## Monitoraggio

### Metriche del Server
Esporre la porta del GRPC Server per monitorare le metriche:
```bash
kubectl port-forward svc/grpc-server 8000:8000 -n dsbd-namespace
```

- Accedi alle metriche dal browser:
  [http://localhost:8000/metrics](http://localhost:8000/metrics)

### Metriche del Data Collector
Esporre la porta del Data Collector per monitorare le metriche:
```bash
kubectl port-forward svc/data-collector 8000:8000 -n dsbd-namespace
```

- Accedi alle metriche dal browser:
  [http://localhost:8000/metrics](http://localhost:8000/metrics)

### Debug dei Pods

1. Controlla lo stato dei pods:
   ```bash
   kubectl get pods -n dsbd-namespace
   ```

2. Per vedere i log di un pod specifico:
   ```bash
   kubectl logs "<nome-pod>" -n dsbd-namespace
   ```

3. Per descrivere un pod e identificare eventuali errori:
   ```bash
   kubectl describe pod "<nome-pod>" -n dsbd-namespace
   
