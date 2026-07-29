from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from run_orchestrator import (
    run_bronze_to_silver,
    upload_silver,
    run_silver_to_gold,
    upload_gold,
)

with DAG(
    dag_id="healthcare_etl",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    bronze_to_silver = PythonOperator(
        task_id="bronze_to_silver",
        python_callable=run_bronze_to_silver,
    )

    upload_silver_task = PythonOperator(
        task_id="upload_silver",
        python_callable=upload_silver,
    )

    silver_to_gold = PythonOperator(
        task_id="silver_to_gold",
        python_callable=run_silver_to_gold,
    )

    upload_gold_task = PythonOperator(
        task_id="upload_gold",
        python_callable=upload_gold,
    )

    bronze_to_silver >> upload_silver_task >> silver_to_gold >> upload_gold_task