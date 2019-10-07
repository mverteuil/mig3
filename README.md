# ![mig3](https://repository-images.githubusercontent.com/183804036/f4e59c00-69bb-11e9-96c5-6188c6a6f664)
## *mig3*: Detect regressions in your python3 migration!

[![Codacy Quality Badge](https://api.codacy.com/project/badge/Grade/79079a3fa54e49d4b6cfee5f3451737e)](https://www.codacy.com/app/mverteuil/mig3?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mverteuil/mig3&amp;utm_campaign=Badge_Grade)
[![Codacy Coverage Badge](https://api.codacy.com/project/badge/Coverage/79079a3fa54e49d4b6cfee5f3451737e)](https://www.codacy.com/app/mverteuil/mig3?utm_source=github.com&utm_medium=referral&utm_content=mverteuil/mig3&utm_campaign=Badge_Coverage)
[![Travis Build Status](https://img.shields.io/travis/com/mverteuil/mig3/master.svg?logo=travis)](https://travis-ci.com/mverteuil/mig3)
[![CircleCI Build Status](https://img.shields.io/circleci/build/github/mverteuil/mig3.svg?logo=circleci)](https://circleci.com/gh/mverteuil/mig3)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3?ref=badge_shield)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/mverteuil/mig3.svg?logo=docker)
![MicroBadger Layers](https://img.shields.io/microbadger/layers/mverteuil/mig3.svg?color=limegreen&logo=docker)
![MicroBadger Size](https://img.shields.io/microbadger/image-size/mverteuil/mig3.svg?color=limegreen&logo=docker)
![GitHub](https://img.shields.io/github/license/mverteuil/mig3.svg?logo=gnu)
[![Manpower](https://img.shields.io/github/contributors/mverteuil/mig3.svg?color=red&label=manpower&logo=github)](https://github.com/mverteuil/mig3/graphs/contributors)
[![Python Code Style: Black](https://img.shields.io/badge/code_style-black-black.svg?logo=python&logoColor=yellow)](https://github.com/python/black)
[![JS Code Style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?logo=javascript)](https://github.com/prettier/prettier)

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
-   Poetry 0.12.17+
-   PostgreSQL 11+

---

## Production Installation

### Standard Installation

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

 *PROTIP*: You need to watch the logs in order to see the *SECRET CODE* (and enter it within 10 minutes) in order to create your initial administrator account. Once you click "Create App", open a new tab to your projects view and click on the new app. Look on the top right for "More" and choose "View Logs".

### Skeleton Installation

```zsh
git clone https://github.com/mverteuil/mig3.git .
poetry install --no-dev
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
poetry install
cd mig3-ui
yarn install
```
then,
```zsh
make devserver  # Build and start detatched containers
```
or
```zsh
make run-dev  # Build and start containers in console
```
or
```zsh
make devserver-db  # Start only the database
```
or
```zsh
make test  # (Start containers and) run test suite
```

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmverteuil%2Fmig3?ref=badge_large)
