.PHONY = clean devserver* db install release run
SHELL := /bin/bash

ACTIVATE = source .venv/bin/activate
SET_CONTEXT := ${ACTIVATE} && cd mig3 && DJANGO_SETTINGS_MODULE=mig3.settings
UP_DETACHED = docker-compose up --build --detach
UP_LIVE = docker-compose up --abort-on-container-exit

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

clean:
	docker-compose down --rmi all --remove-orphans

devserver: devserver-db devserver-frontend devserver-backend
	@echo "Started development servers."
	@echo "Django Dev Server: http://localhost:8000/"
	@echo "Vue Dev Server: http://localhost:8080/"
	@echo "PostgreSQL Server: postgresql://postgres:postgres@localhost:15432/postgres"

devserver-%:
	${UP_DETACHED} $${$@}

run-dev:
	@echo "Starting development servers."
	@echo "Django Dev Server: http://localhost:8000/"
	@echo "Vue Dev Server: http://localhost:8080/"
	@echo "PostgreSQL Server: postgresql://postgres:postgres@localhost:15432/postgres"
	${UP_LIVE}
