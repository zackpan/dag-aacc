from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

dag = DAG(dag_id='standard_ops', schedule_interval=None, tags=['aacc'])

task = BashOperator(
    task_id='dummy_task',
    dag=dag,
    bash_command="sleep 10",
    start_date=days_ago(2),
    owner='airflow',
)
