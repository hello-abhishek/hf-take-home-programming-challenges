## Data Engineer task solution

ETL job that ingest data from API, sort the data, and determine top ten favorite menu.

The data pipeline consists on the following steps:
- ingestion task: ingest the dataset from API asynchronously using httpx
- transformation task: sort the data set by ratings and favorite count, and then get the top 10 menu
- load task: sink the transformed data into specify folder

### Execution instructions

The repo includes a `Makefile`. Please run `make help` to see usage

