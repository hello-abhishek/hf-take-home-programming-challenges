from airflow import DAG
from datetime import datetime

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from dags.job.recipe_job import run, sink_to_csv, recipes, top_ten, sort_by_rating_favourite, \
    replace_none_with_empty_str, menus_data, recipes_sorted, sink_top_ten, top_ten_menu, get_data

import logging
import asyncio
from datetime import date, datetime
from operator import itemgetter

import httpx
import csv

dag = DAG(
    'classic_menu_etl',
    start_date=datetime(2021, 10, 28),
    catchup=False,
    schedule_interval='@weekly',
)

recipe = BashOperator(
    task_id='etl_recipe',
    bash_command='python /airflow/dags/job/recipe_job.py',
    dag=dag
)

# get_data = PythonOperator(
#     task_id='greet',
#     python_callable=get_data,
#     dag=dag
# )

# cleaned_menus = [replace_none_with_empty_str(menu) for menu in menus_data[0]]
#
# get_recipe_data = PythonOperator(
#     task_id='get_recipe_data',
#     dag=dag,
#     python_callable=run
# )
#
# sink_to_csv = PythonOperator(
#     task_id='sink_to_csv',
#     dag=dag,
#     python_callable=sink_to_csv,
#     op_kwargs={'recipes': recipes}
# )

# cleaned_menus = [replace_none_with_empty_str(menu) for menu in menus_data[0]]

# sort_by_rating_favourite = PythonOperator(
#     task_id='sort_by_rating_favourite',
#     dag=dag,
#     python_callable=sort_by_rating_favourite,
#     op_kwargs={'menus': cleaned_menus}
# )
#
# top_ten = PythonOperator(
#     task_id='top_ten',
#     dag=dag,
#     python_callable=top_ten,
#     op_kwargs={'menus': recipes_sorted[0]}
# )
#
# sink_top_ten = PythonOperator(
#     task_id='sink_top_ten',
#     dag=dag,
#     python_callable=sink_top_ten,
#     op_kwargs={'top_ten_menu': top_ten_menu}
# )

recipe
