# Create your app image
```sh
docker build . -t eda-ingestion-app:0.0.1
```

# Load into your minikube cluster
```sh
minikube image load eda-ingestion-app:0.0.2
```

# Create your namespace
```sh
kubectl create ns ingestion-app
```

# Test your app
```sh
kubectl apply -f app-test.yaml
```

# Apply your app as a cronjob
```sh
kubectl apply -f app-cronjob.yaml
```