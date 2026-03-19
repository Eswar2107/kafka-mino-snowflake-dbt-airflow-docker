from airflow.decorators import dag, task
from pendulum import datetime

DBT_PROJECT_PATH = r"/opt/airflow/dbt/dbt_stocks"

@dag(
    dag_id='dbt_dag',
    start_date=datetime(year=2026, month=3, day=13, tz="Europe/Paris"),
    schedule="@daily",
    is_paused_upon_creation=False,
    catchup=True
)
def dbt_dag():

    @task.bash
    def run_bronze():
        return f"""
        cd {DBT_PROJECT_PATH} && 
        dbt run --select bronze_stg_stock_quotes
        """

    @task.bash
    def run_silver():
        return f"""
        cd {DBT_PROJECT_PATH} && 
        dbt run --select path:models/silver
        """

    @task.bash
    def run_gold():
        return f"""
        cd {DBT_PROJECT_PATH} && 
        dbt run --select path:models/gold
        """

    task1 = run_bronze()
    task2 = run_silver()
    task3 = run_gold()

    task1 >> task2 >> task3


dbt_dag()