# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pip==19.1.1 pipenv==2018.11.26
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev 2>/dev/null

# Copy project root
COPY . docker/runserver.sh /code/
CMD /code/docker/runserver.sh
