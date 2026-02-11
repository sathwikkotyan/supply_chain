from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def health_check():
    paths = [
        "/home/sathwik/supply_chain_project",
        "/home/sathwik/supply_chain_project/Data_generation",
        "/home/sathwik/supply_chain_project/kafka_producer"
    ]
    for path in paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing path: {path}")
    print("✅ Supply Chain Health Check Passed")

with DAG(
    dag_id="supply_chain_health_check",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["starter", "supply_chain"]
) as dag:

    health_check_task = PythonOperator(
        task_id="health_check_task",
        python_callable=health_check
    )
