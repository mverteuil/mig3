# Pull base image
FROM node:12.2-stretch

# Set work directory
WORKDIR /code

# Install dependencies
COPY package.json yarn.lock /code/
RUN yarn install

# Copy project root
COPY . /code/
