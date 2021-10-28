from airflow import DAG
from datetime import datetime

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
# from dags.job.recipe_job import run, sink_to_csv, recipes, top_ten, sort_by_rating_favourite, \
#     replace_none_with_empty_str, menus_data, recipes_sorted, sink_top_ten, top_ten_menu, get_data

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
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

response = []
recipes = []
menus_data = []
recipes_sorted = []
top_ten_menu = []

date_now = datetime.today().strftime("%Y_%W")


async def fetch(client: any):
    return await client.get(f"https://e075-158-140-191-48.ngrok.io", timeout=None)


async def recipe_data():
    async with httpx.AsyncClient() as client:
        responses = await asyncio.gather(fetch(client))
        return responses


def run_async_task(c, coro=None):
    """
        A helper class to create async coroutines.
        :param coro: a valid coroutine
        :return: result set from the async function
        """
    if coro is None:
        coro = c

    results = asyncio.run(coro)
    return results


def extract_data(response: list) -> None:
    """Extract data from response"""
    for data in response:
        try:
            results = data.json()
            recipes.append(results[0])
        except Exception as e:
            logger.error("cannot get the response")
            raise e


def sink_to_csv(recipes: list) -> None:
    data = [recipe['recipe'] for recipe in recipes[0]]

    header = data[0].keys()

    with open(f'output/{date_now}_menu.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, header)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    return menus_data.append(data)


def sort_by_rating_favourite(menus: list) -> None:
    """Sort the menu by ratings and then favourite"""
    sorted_menu = sorted(menus, key=itemgetter('ratingsCount', 'favoritesCount'), reverse=True)
    return recipes_sorted.append(sorted_menu)


def top_ten(menus: list) -> None:
    """show only top ten of sorted menu"""
    return top_ten_menu.append(menus[:10])


def sink_top_ten(top_ten_menu: list) -> None:
    data = top_ten_menu[0]

    header = data[0].keys()
    with open(f'output/{date_now}_top_10.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, header)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def run() -> list:
    extract_data(run_async_task(recipe_data()))
    return recipes


def replace_none_with_empty_str(some_dict: dict) -> dict:
    return {k: (0 if v is None else v) for k, v in some_dict.items()}

def extract_recipe_data(recipes):
    data = [recipe['recipe'] for recipe in recipes[0]]
    menus_data.append(data)


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
