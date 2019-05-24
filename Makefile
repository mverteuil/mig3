.PHONY = check-dev clean devserver* full-clean install release run run-dev stop-dev
SHELL := /bin/bash

# ^^^^^^ Global Above ---------- Production Below VVVVVV

ACTIVATE = source .venv/bin/activate
SET_CONTEXT := ${ACTIVATE} && cd mig3 && DJANGO_SETTINGS_MODULE=mig3.settings

.venv:
	python3 -m venv .venv

install: .venv
	${ACTIVATE} && pip install --upgrade pip pipenv==2018.11.26 && pipenv install --deploy
	${ACTIVATE} && barb -t .env.production.yml -z

release:
	${SET_CONTEXT} python manage.py migrate
	${SET_CONTEXT} python manage.py collectstatic --no-input

run: release
	${SET_CONTEXT} python manage.py check
	${SET_CONTEXT} gunicorn mig3.wsgi --bind 0:8000 --workers 4 --log-file -

# ^^^^^^ Production Above ----- Development Below VVVVVV

EXEC_LIVE = docker-compose exec
PROJECT_DIR = $(shell basename $(CURDIR))
TEARDOWN = docker-compose down
UP_DETACHED = docker-compose up --detach
UP_LIVE = docker-compose up --abort-on-container-exit

check-dev:
	@$(EXEC_LIVE) backend python mig3/manage.py check --fail-level WARNING

clean:
	@docker-compose down --rmi all --remove-orphans || true
	@docker volume rm $(PROJECT_DIR)_postgres_data || true

full-clean: clean
	@docker container prune -f
	@docker image prune -f

devserver:
	@echo "Starting development servers..."
	@$(UP_DETACHED)
	@echo "PostgreSQL Server: postgresql://postgres:postgres@localhost:15432/postgres"
	@echo "Vue Dev Server: http://localhost:8080/"
	@echo "Django Dev Server: http://localhost:8000/"

devserver-%:
	@$(UP_DETACHED) $${$@}

run-dev: | devserver check-dev
	@$(UP_LIVE) backend

stop-dev:
	@$(TEARDOWN)
