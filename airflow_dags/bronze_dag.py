from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

BRONZE_PATH = "/home/sathwik/supply_chain_project/Supply_chain_project/data/bronze"

def validate_bronze():
    if not os.path.exists(BRONZE_PATH):
        raise Exception("Bronze folder missing")
    if not os.listdir(BRONZE_PATH):
        raise Exception("No raw data in Bronze layer")
    print("Bronze layer validated")

with DAG(
    dag_id="bronze_validation_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    tags=["bronze"]
) as dag:
    validate = PythonOperator(
        task_id="validate_bronze",
        python_callable=validate_bronze
    )
