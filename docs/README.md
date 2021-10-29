## Data Engineer task solution

ETL job that ingest data from API, sort the data, and determine top ten favorite menu.

The data pipeline consists on the following steps:
- ingestion task: ingest the dataset from API asynchronously using httpx
- transformation task: sort the data set by ratings and favorite count, and then get the top 10 menu
- load task: sink the transformed data into specify folder (/output folder)

This job will run once a week by apache airflow. The dags will be found in `dags` folder.

### Overview

The data pipeline run automatically once a week by apache airflow. The output data will saved in `output` folder under `dags`
folder.

The ETL job scripts can be found in `recipe_job.py`, this file consists several method that runs ETL steps.

`fetch` : This method responsible to connect to API

`recipe_data`: Responsible for get the response from what `fetch` do

`run_async_task`: Get the result set asynchronously

`extract_data`: Save the data to list `recipes` for further implementation

`sink_to_csv`: Get `recipe` data and save it to CSV with specific name

`sort_by_rating_favourite`: sort the `recipe` list by ratings and favorite counts

`top_ten`: Collect only top ten of the most popular menu

`sink_top_ten`: Save the top ten menu into CSV

`run`: run fetch, recipe_data, run_async_task, and extract_data sequentially

### Execution instructions

The repo includes a `Makefile`. Please run `make help` to see usage.

