# Pull base image
FROM node:12.2-stretch

# Set work directory
WORKDIR /code

# Install dependencies
COPY mig3-ui/package.json mig3-ui/yarn.lock /code/
RUN yarn install

# Copy project root
COPY mig3-ui /code/
CMD yarn serve
