from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Avinash",
}

with DAG(
    dag_id="healthcare_etl",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    tags=["healthcare"],
) as dag:

    silver = BashOperator(
        task_id="silver_layer",
        bash_command="""
        cd /opt/project
        export PYTHONPATH=src
        python src/run_all_pipelines.py
        """,
    )

    gold = BashOperator(
        task_id="gold_layer",
        bash_command="""
        cd /opt/project
        export PYTHONPATH=src
        python src/run_all_gold.py
        """,
    )

    silver >> gold