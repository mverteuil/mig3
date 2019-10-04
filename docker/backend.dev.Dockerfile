# Pull base image
FROM python:3.7
SHELL ["/bin/bash", "-c"]

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install poetry && python3 -m venv .venv
COPY pyproject.toml poetry.lock /code/
RUN source .venv/bin/activate && poetry install

# Copy project root
COPY . /code/
CMD /code/docker/runserver.sh
