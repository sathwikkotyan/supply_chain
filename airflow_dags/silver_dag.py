from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

SILVER_PATH = "/home/sathwik/supply_chain_project/Supply_chain_project/data/silver"

def transform_to_silver():
    os.makedirs(SILVER_PATH, exist_ok=True)
    print("Silver layer ready (transform simulated)")

with DAG(
    dag_id="silver_transformation_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    tags=["silver"]
) as dag:
    transform = PythonOperator(
        task_id="transform_to_silver",
        python_callable=transform_to_silver
    )
