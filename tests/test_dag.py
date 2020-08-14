
import glob
from os import path

import pytest
from airflow import models as airflow_models

DAG_PATHS = glob.glob(path.join(path.dirname(__file__), "..", "*.py"))


@pytest.mark.parametrize("dag_path", DAG_PATHS)
def test_dag_integrity(dag_path):
    dag_name = path.basename(dag_path)
