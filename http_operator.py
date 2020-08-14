from airflow.models import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.utils.dates import days_ago

dag = DAG(dag_id='fis_schedules', schedule_interval=None, tags=['fis'])
task_get_op = SimpleHttpOperator(
    task_id='get_op',
    method='GET',
    endpoint='get',
    data={"param1": "value1", "param2": "value2"},
    headers={},
    dag=dag,
)