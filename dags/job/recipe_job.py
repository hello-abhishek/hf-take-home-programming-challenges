import logging
import asyncio
from datetime import date, datetime
from operator import itemgetter

import httpx
import csv

from pip._vendor import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

response = []
recipes = []
menus_data = []
recipes_sorted = []
top_ten_menu = []

date_now = datetime.today().strftime("%Y_%W")


async def fetch(client: any):
    return await client.get(f"https://623c-158-140-191-48.ngrok.io", timeout=None)


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

def get_data():
    r = requests.get("https://623c-158-140-191-48.ngrok.io")
    return r.json


def extract_data(response: list) -> list:
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

    with open(f'/airflow/dags/output/{date_now}_menu.csv', 'w', newline='') as output_file:
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
    with open(f'/airflow/dags/output/{date_now}_top_10.csv', 'w', newline='') as output_file:
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



if __name__ == '__main__':
    run()
    sink_to_csv(recipes)
    cleaned_menus = [replace_none_with_empty_str(menu) for menu in menus_data[0]]
    sort_by_rating_favourite(cleaned_menus)
    top_ten(recipes_sorted[0])
    sink_top_ten(top_ten_menu)
