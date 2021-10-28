SHELL=/bin/bash

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-rm:
	docker-compose rm -fs

setup:
	pip install --upgrade pip setuptools && pip install -r requirements.txt

airflow-start:
	python wait_for_db.py
	airflow db init
	airflow users create -u ${AIRFLOW_ADMIN_USER} -p ${AIRFLOW_ADMIN_PASSWORD} -r Admin -e admin@admin.com -f admin -l admin
	airflow webserver -D
	airflow scheduler