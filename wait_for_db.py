import pandas as pd
import os
import sqlalchemy
import time

# Wait for Airflow DB to be ready

conn_string = os.environ['AIRFLOW__CORE__SQL_ALCHEMY_CONN']
error = True

while error:
    try:
        print('Trying to connect to AirflowDB...')
        pd.read_sql('select 1;', conn_string)
        print('Airflow DB is up!')
        error = False
    except sqlalchemy.exc.OperationalError as e:
        print(f"Cannot connect to Airflow DB with connection string: {conn_string}\n"
              f"The error is: {str(e)}\n"
              f"Trying again...")
        time.sleep(3)
        continue