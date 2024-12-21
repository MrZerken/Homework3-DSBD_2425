minikube start

installa minikube da questo link: https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download

scarica kubectl da qui: https://kubernetes.io/releases/download/#binaries
seleziona la v1.32.0 amd64 kubectl, una volta scaricato prendi quel file lo metti dove vuoi e lo aggiungi alle variabili d'ambiente


kubectl create namespace dsbd-namespace


#per far si che targhettiamo docker-env e ci costruiamo le immagini dentro
minikube docker-env | Invoke-Expression


#per buildare le immagini custom dei container
docker build -t grpc-server:latest -f Dockerfile.server .        
docker build -t data-collector:latest -f Dockerfile.datacollector .
docker build -t cp_alertsystem:latest -f Dockerfile.cp_alertsystem .
docker build -t c_alertnotifiersystem:latest -f Dockerfile.c_alertnotifiersystem .


#per caricare i manifest
kubectl apply -f ./manifests/ -n dsbd-namespace  


#per vedere lo stato dei pods, aspetta tutti siano in stato running prima di procedere
kubectl get pods -n dsbd-namespace 


#per esporre la porta del server e poter usare il client
kubectl port-forward svc/grpc-server 18072:18072 -n dsbd-namespace 


#
#Da qui in poi tutto debugging
#

#per esporre la porta del server e vedere le metriche 
kubectl port-forward svc/grpc-server 8000:8000 -n dsbd-namespace 

E poi andare su browser su http://localhost:8000/metrics

#per esporre la porta del data-collector e vedere le metriche 
kubectl port-forward svc/data-collector 8000:8000 -n dsbd-namespace 

E poi andare su browser su http://localhost:8000/metrics


#Se vuoi controllare lo stato dei pods o i log o per vedere perchè sono crashati fai 

kubectl get pods -n dsbd-namespace 

poi fai copia e incolla del nome e fai uno di questi due comandi o entrambi (danno info diverse)

kubectl logs "inserisci qui in nome senza apici" -n dsbd-namespace

kubectl describe pod "inserisci qui in nome senza apici" -n dsbd-namespace
