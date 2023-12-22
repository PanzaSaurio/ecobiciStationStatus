#dag_ecobiciStationStatus.py

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from scripts.ecobiciStationStatus import process_station_data
# from scripts.ecobiciStationStatus import main

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
    dag_id="dag_ecobiciStationStatus",
    start_date = datetime(2023, 12, 5),
    catchup = False,
    schedule_interval = "0 * * * *",
    default_args = default_args
) as dag:
    

    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="redshift",
        sql="sql/ecobici_stations.sql",
        hook_params = {'options': '-c search_path=reyna_mario_coderhouse'}
        )

    main_task = PythonOperator(
        task_id='main_task',
        python_callable= process_station_data, #main,
        op_kwargs={'config': '/opt/airflow/config/credentials.json'}
        )


    create_table >> main_task