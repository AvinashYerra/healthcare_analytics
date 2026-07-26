from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime


with DAG(

    dag_id="healthcare_etl",

    start_date=datetime(2026, 1, 1),

    schedule="@daily",

    catchup=False,

    tags=["healthcare"],

) as dag:

    run_etl = BashOperator(

        task_id="run_healthcare_etl",

        bash_command="""
        cd /opt/project &&
        python run_orchestrator.py
        """,
    )