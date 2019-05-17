FROM node:12.2-stretch AS UI
# Set work directory
WORKDIR /code

# Install dependencies
COPY mig3-ui/package.json mig3-ui/yarn.lock /code/
RUN yarn install
# Copy project root
COPY mig3-ui /code/
# Build frontend
RUN yarn build

# ---

FROM python:3.7

# Use bash for `source` in makefile
SHELL ["/bin/bash", "-c"]
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install Backend
COPY . /code/

# Install UI
COPY --from=UI /code/dist /code/mig3-ui/dist

# Install dependencies
RUN pip install pipenv==2018.11.26
RUN make install

CMD make run
