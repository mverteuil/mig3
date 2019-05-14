# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv==2018.11.26
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

# Generate environment variables if they don't already exist
COPY .env.yml /code/
RUN barb -z

# Copy project root
COPY . /code/
