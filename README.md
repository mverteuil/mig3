![Mig3](https://repository-images.githubusercontent.com/183804036/f4e59c00-69bb-11e9-96c5-6188c6a6f664)

# Detect regressions in your python3 migration!

[![Codacy Quality Badge](https://api.codacy.com/project/badge/Grade/8fbaac0868ee4261915b7c48ba8ee881)](https://app.codacy.com/app/mverteuil/mig3?utm_source=github.com&utm_medium=referral&utm_content=mverteuil/mig3&utm_campaign=Badge_Grade_Dashboard)
[![Codacy Coverage Badge](https://api.codacy.com/project/badge/Coverage/79079a3fa54e49d4b6cfee5f3451737e)](https://www.codacy.com/app/mverteuil/mig3?utm_source=github.com&utm_medium=referral&utm_content=mverteuil/mig3&utm_campaign=Badge_Coverage)
[![Build Status](https://travis-ci.com/mverteuil/mig3.svg?branch=master)](https://travis-ci.com/mverteuil/mig3)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3?ref=badge_shield)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

# Production Requirements

-   Python 3.7+
-   Pipenv
-   PostgreSQL 11+

# Production Installation

```
$ git clone https://github.com/mverteuil/mig3.git .
$ pipenv install --deploy
$ pipenv run barb  # Or "barb-deploy -z" in advanced AWS configuration
$ pipenv run python mig3/manage.py migrate
$ pipenv run python mig3/manage.py createsuperuser --email <your@email.address>
$ pip install gunicorn  # or preferred alternative
```

# Development Requirements

-   Docker (optional, but helpful)
-   Pre-Commit 1.15+

# Development Installation

```
$ git clone https://github.com/mverteuil/mig3.git .
$ pre-commit install
$ pipenv install --dev
$ pipenv shell
$ barb -z
$ docker-compose up --detach  # or without "--detach" in another terminal session
$ python mig3/manage.py migrate
$ python mig3/manage.py createsuperuser --email <your@email.address>
```

It's recommended that you validate your installation at this point by confirming that linters and tests are passing as expected:

```
$ py.test && pre-commit run --all-files && echo "VALIDATED\!" || echo "CHECK YOUR INSTALLATION"
```

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3?ref=badge_large)
