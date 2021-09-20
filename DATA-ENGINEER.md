# Data Engineer

## Data-pipeline Focused

### Problem Statement
Create a [Airflow](https://airflow.apache.org/) pipeline which runs once a week. 

#### Context
- A [weekly menu](https://www.hellofresh.com/plans/) contains a set of [recipies](https://www.hellofresh.com/recipes/). Each week different set of recipies are selected. See example [menu for this week](https://www.hellofresh.com/plans/).
- A [recipe](https://www.hellofresh.com.au/recipes/beef-veggie-ragu-spaghetti-5fa9c324cb8f8c0b3a183d01) contains ingredients, step-by-step instructions, nutirtional information, classification, and other metadata. See examples recipes here [1](https://www.hellofresh.com.au/recipes/southeast-asian-chicken-coconut-soup-5fa9c26209c8db59115d3f4f), [2](https://www.hellofresh.com.au/recipes/saucy-coconut-chicken-noodles-5f9b3c7198ecf4455b27d94d), [3](https://www.hellofresh.com.au/recipes/dukkah-roasted-sweet-potato-5f9b43847aacaa50f037d858).
- A customer can review weekly menu as well as recipe by assigning ratings and/or adding comments.

#### Tasks
Create Data pipeline (DAG) in Python and/or Go Language with following steps:

- Retrieve all recipes for current week menu using API call (Review [Mock API](https://hellofresh-au.free.beeceptor.com/menus/2021-W10/classic-box))
- For each recipe extract following information from API resposen: `name`, `headline`, `prepTime`, `ratingsCount`, `favoritesCount`, `nutrition - Energy (kJ)`, etc.
- Data must be flattened into a CSV file. CSV Filename: `YYYY_WW_menu.csv`.
- Identify top 10 recipes based on `ratingsCount`, `favoritesCount` and export them a file `YYYY_WW_TOP_10.csv`. 
- Result CSV must be uploaded to the following s3 location `s3_bucket/YYYY_WW_menu.csv` and `s3_bucket/YYYY_WW_TOP_10.csv`.

In addtion,
- The solution must be able run on-demand via `make` command.
- Include `Dockerfile` so solution can be run as container
- Create [Helm chart](https://helm.sh/) so solution can be deployed to Kubernetes cluster
- Create unit, integration, and e2e test as applicable to ensure pipeline can be tested
- Create a Github action based CI/CD pipieline to run the tests and deploy to Kubernetes cluster
- Provide a comprehensive `README` file with notes on how to run locally and overall system design

