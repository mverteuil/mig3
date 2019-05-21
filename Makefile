.PHONY = clean devserver* install release run run-dev
SHELL := /bin/bash

# ^^^^^^ Global Above ---------- Production Below VVVVVV

ACTIVATE = source .venv/bin/activate
SET_CONTEXT := ${ACTIVATE} && cd mig3 && DJANGO_SETTINGS_MODULE=mig3.settings

.venv:
	python3 -m venv .venv

install: .venv
	${ACTIVATE} && pip install pipenv==2018.11.26 && pipenv install --deploy
	${ACTIVATE} && barb -z

release:
	${SET_CONTEXT} python manage.py migrate

run:
	${SET_CONTEXT} python manage.py check
	${SET_CONTEXT} gunicorn mig3.wsgi --log-file -

# ^^^^^^ Production Above ----- Development Below VVVVVV

PROJECT_DIR := $(shell basename $$PWD)
DJANGO_CHECKS = docker-compose exec backend python mig3/manage.py check --fail-level WARNING
UP_DETACHED = docker-compose up --build --detach
UP_LIVE = docker-compose up --abort-on-container-exit

clean:
	docker-compose down --rmi all --remove-orphans
	docker volume rm ${PROJECT_DIR}_postgres_data

devserver:
	@echo "Starting development servers..."
	${UP_DETACHED}
	@echo "PostgreSQL Server: postgresql://postgres:postgres@localhost:15432/postgres"
	@echo "Vue Dev Server: http://localhost:8080/"
	@echo "Django Dev Server: http://localhost:8000/"
	${DJANGO_CHECKS}

devserver-%:
	${UP_DETACHED} $${$@}

run-dev: devserver
	${UP_LIVE}
