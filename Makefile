.PHONY = clean dev-install install release run

SHELL := /bin/bash


mig3-ui/node_modules:
	cd mig3-ui && yarn install --prod

mig3-ui/dist: mig3-ui/node_modules
	cd mig3-ui && yarn build

.venv:
	python3 -m venv .venv

release:
	.venv/bin/python mig3/manage.py migrate

run:
	source .venv/bin/activate && cd mig3 && DJANGO_SETTINGS_MODULE=mig3.settings python manage.py check
	source .venv/bin/activate && cd mig3 && DJANGO_SETTINGS_MODULE=mig3.settings gunicorn mig3.wsgi

dev-install:
	docker-compose up --build

install: mig3-ui/dist .venv
	source .venv/bin/activate && pip install pipenv==2018.11.26 && pipenv install --deploy
	source .venv/bin/activate && barb -z

clean:
	rm -rf .venv/
	rm -rf mig3-ui/dist
	rm -rf mig3-ui/node_modules
	rm .env
