# ![mig3](https://repository-images.githubusercontent.com/183804036/f4e59c00-69bb-11e9-96c5-6188c6a6f664)
## *mig3*: Detect regressions in your python3 migration!

[![Codacy Quality Badge](https://api.codacy.com/project/badge/Grade/79079a3fa54e49d4b6cfee5f3451737e)](https://www.codacy.com/app/mverteuil/mig3?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mverteuil/mig3&amp;utm_campaign=Badge_Grade)
[![Codacy Coverage Badge](https://api.codacy.com/project/badge/Coverage/79079a3fa54e49d4b6cfee5f3451737e)](https://www.codacy.com/app/mverteuil/mig3?utm_source=github.com&utm_medium=referral&utm_content=mverteuil/mig3&utm_campaign=Badge_Coverage)
[![Build Status](https://travis-ci.com/mverteuil/mig3.svg?branch=master)](https://travis-ci.com/mverteuil/mig3)
[![CircleCI](https://circleci.com/gh/mverteuil/mig3.svg?style=svg)](https://circleci.com/gh/mverteuil/mig3)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3?ref=badge_shield)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

## See Also

-   [mig3-client](https://github.com/mverteuil/mig3-client): Submit your results to this service.

## Deployment Methods

| *Name*                    | Standard | Skeleton |
|---------------------------|:--------:|:--------:|
| Prevents Regressions      |     ✈    |     ✈    |
| Python3 Required          |     ✈    |     ✈    |
| Node Required             |     ✈    |          |
| Admin User Interface      |     ✈    |     ✈    |
| Standard User Interface   |     ✈    |          |
| Stylish and Cool          |     ✈    |          |
| People Will Like You†     |     ✈    |          |

*†* Probably not true

## Production Dependency Suggestions

You may find success running with earlier versions of these dependencies, but these are the ideal set which the project
was designed to be supported by:

### Standard Dependencies

-   Python 3.7+
-   Pip 19+
-   PostgreSQL 11+
-   Node 12+
-   Yarn 1.16+

### Skeleton Dependencies

-   Python 3.7+
-   Pip 19+
-   Pipenv 2018.11.26+
-   PostgreSQL 11+

---

## Production Installation

### Standard Installation

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Skeleton Installation

```zsh
git clone https://github.com/mverteuil/mig3.git .
pipenv install --deploy
pipenv run pip install gunicorn
```

---

## Development Requirements

-   All standard production requirements
-   Docker 18.09.2+
-   docker-compose 1.23.2+
-   Pre-Commit 1.15+

## Development Installation

If you're simply interested in running mig3 locally to play around with it:
```zsh
git clone https://github.com/mverteuil/mig3.git .
make run-dev
```

What follows are the instructions for getting started with actual mig3 development:

```zsh
git clone https://github.com/mverteuil/mig3.git .
pre-commit install
pipenv install
cd mig3-ui
yarn install
```
then,
```zsh
make devserver  # build and start detatched containers
```
or
```zsh
make run-dev  # build and start containers in console
```
or
```zsh
make devserver-db  # Start only the database
```
It's recommended that you validate your installation at this point by confirming that linters and tests are passing as expected:

```zsh
py.test && pre-commit run --all-files && echo "VALIDATED\!" || echo "CHECK YOUR INSTALLATION"
```

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3?ref=badge_large)
