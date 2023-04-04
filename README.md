# Providing our POC cluster 

```sh
minikube start --nodes 3 --memory 16384 --cpus 2 --driver=virtualbox --disk-size 200GB
```

# Installing AIRFLOW using HELM
- Setting up helm
```sh
helm repo add apache-airflow https://airflow.apache.org/
helm pull apache-airflow/airflow
tar zxvf airflow-1.8.0.tgz
mv airflow kubernetes/charts/airflow
rm -rf airflow-1.8.0.tgz
```

```sh
helm install airflow kubernetes/charts/airflow -n airflow --create-namespace --debug
```

# Setting up a DBT project
```sh
pip install dbt-postgres
```

