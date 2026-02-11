from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(
    dag_id="supply_chain_master_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    bronze = TriggerDagRunOperator(
        task_id="trigger_bronze",
        trigger_dag_id="bronze_validation_dag"
    )

    silver = TriggerDagRunOperator(
        task_id="trigger_silver",
        trigger_dag_id="silver_transformation_dag"
    )

    gold = TriggerDagRunOperator(
        task_id="trigger_gold",
        trigger_dag_id="gold_publish_dag"
    )

    bronze >> silver >> gold
