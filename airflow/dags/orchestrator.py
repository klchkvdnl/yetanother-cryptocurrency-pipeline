import sys
from pendulum import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

# that is for importing inside container
sys.path.append('/opt/airflow/api_request')
from insert_records import main


with DAG(
    dag_id='crypto-currency-api-dbt-orchestrator',
    default_args={
        'owner':'user'
    },
    start_date=datetime(2026, 3, 5, tz='UTC'),
    schedule='* * * * *'
) as dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=main
    )

    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(
                # here add YOUR absolute path to ./dbt/my_project
                source='/home/jsttl600/code/1_yetanother_cryptocurrency_pipeline/yetanother-cryptocurrency-pipeline/dbt/my_project',
                target='/usr/app',
                type='bind'
            ),
            Mount(
                # here add YOUR absolute path to /dbt/profiles.yml
                source='/home/jsttl600/code/1_yetanother_cryptocurrency_pipeline/yetanother-cryptocurrency-pipeline/dbt/profiles.yml',
                target='/root/.dbt/profiles.yml',
                type='bind'
            )
        ],
        # here add your network: use docker network ls to find it
        network_mode='yetanother-cryptocurrency-pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2