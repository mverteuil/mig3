.PHONY = check-dev clean devserver* full-clean install release run run-dev stop-dev

SHELL    := /bin/bash
PROGRESS ?= tty

help: 																 ## Display help for developer targets
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%-30s %s\n" "target" "help" ; \
	printf "%-30s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-30s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done

# ^^^^^^ Global Above ---------- Production Below VVVVVV

ACTIVATE     = source /data/venv/bin/activate
PORT         = $(shell echo $${PORT:-8000})
SET_CONTEXT := $(ACTIVATE) && cd mig3 && DJANGO_SETTINGS_MODULE=mig3.settings

.venv:
	python3 -m venv .venv

install: .venv
	$(ACTIVATE) && pip install --upgrade pip poetry==0.12.17 && poetry install
	$(ACTIVATE) && barb -t .env.production.yml -z

release:
	$(ACTIVATE) poetry install
	$(SET_CONTEXT) python manage.py migrate
	$(SET_CONTEXT) python manage.py collectstatic --no-input

run: release
	$(SET_CONTEXT) python manage.py check
	$(SET_CONTEXT) gunicorn mig3.wsgi --bind 0:$(PORT) --workers 4 --log-file -

# ^^^^^^ Deploy Above --------- Development Below VVVVVV

BUILD       = DOCKER_BUILDKIT=1 docker build . --progress ${PROGRESS} --build-arg
EXEC_LIVE   = docker-compose exec
PROJECT_DIR = $(shell basename $(CURDIR))
TEARDOWN    = docker-compose down
UP_DETACHED = docker-compose up --detach
RUN_LIVE    = docker-compose run

check-dev:                                                           ## Execute checks
	@$(EXEC_LIVE) backend /data/venv/bin/python3 mig3/manage.py check --fail-level WARNING

clean:                                                               ## Destroy containers and images
	@$(TEARDOWN) --rmi all --remove-orphans || true

nuclear-option: clean                                                ## Destroy ALL containers and images / destroy db volume. You probably never want to do this.
	@docker container prune -f
	@docker image prune -a -f
	@docker volume rm $(PROJECT_DIR)_postgres_data || true

devserver-%:
	@${BUILD} BUILD_TARGET=$${$@}-dev -t mig3-$${$@}-dev
	@$(UP_DETACHED) $${$@}

devserver:                                                           ## Start all containers
	@echo "Building development servers..."
	@${BUILD} BUILD_TARGET=backend-dev -t mig3-backend-dev
	@${BUILD} BUILD_TARGET=frontend-dev -t mig3-frontend-dev
	@echo "Starting development servers..."
	@$(UP_DETACHED)
	@echo "PostgreSQL Server: postgresql://postgres:postgres@localhost:15432/postgres"
	@echo "Vue Dev Server: http://localhost:8080/"
	@echo "Django Dev Server: http://localhost:8000/"

run-dev: | devserver check-dev                                        ## Start all containers, then tail backend.
	@$(RUN_LIVE) backend

stop-dev:                                                             ## Gracefully stop containers.
	@$(TEARDOWN)
