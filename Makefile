.PHONY = clean install run

.env:
	barb

mig3-ui/node_modules:
	cd mig3-ui && yarn install

mig3-ui/dist: mig3-ui/node_modules
	cd mig3-ui && yarn build

.venv:
	python3 -m venv .venv

run:
	source .venv/bin/activate && cd mig3 && gunicorn mig3.wsgi

install: mig3-ui/node_modules mig3-ui/dist .venv
	source .venv/bin/activate && pip install pipenv==2018.11.26 && pipenv install --deploy
	source .venv/bin/activate && pip install gunicorn

clean:
	rm -rf .venv/
	rm -rf mig3-ui/dist
	rm -rf mig3-ui/node_modules
	rm .env
