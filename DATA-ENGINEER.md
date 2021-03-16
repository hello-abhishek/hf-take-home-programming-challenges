# Data Engineer

## Data-pipeline Focused

### Problem Statement
Create a Airflow pipeline which runs once a week. 

#### Context

#### Tasks
Data pipeline will:

- Retrieve all recipes for current week menu using API call (Review [Mock API](https://hellofresh-au.free.beeceptor.com/menus/2021-W10/classic-box))
- For each recipe extract following information from API resposen: name, headline, prepTime, ratingsCount, favoritesCount, nutrition - Energy (kJ).
- Data must be flattened into a CSV file. CSV Filename: <pipeline_execution_date>_top_headlines.csv
- Result CSV must be uploaded to the following s3 location <s3_bucket>/<week>/<source_name>
- The solution must be able run on-deman via make command.
