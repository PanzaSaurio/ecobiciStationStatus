from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from scripts.vehicleData import process_vehicle_data

default_args = {
    "owner": "airflow",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "start_date": datetime(2023, 12, 5)
}

dag_id = "dag_vehicle_position_data"
schedule = "30 * * * *"

with DAG(
    dag_id=dag_id,
    schedule_interval=schedule,
    default_args=default_args,
    catchup=False
) as dag:
    

    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="redshift",
        sql="sql/vehicle_positions.sql",
        hook_params = {'options': '-c search_path=reyna_mario_coderhouse'}
        )

    process_vehicle_data_task = PythonOperator(
        task_id='process_vehicle_data',
        python_callable=process_vehicle_data,
        op_kwargs={
            'config': '/opt/airflow/config/credentials.json',
            'agency_id': 49  
        }
    )

    create_table >> process_vehicle_data_task
