# Environment
# ----------------------------------------------------------------------------------------------------------------------
# Target to use for final image
# Valid choices: backend-dev, frontend-dev, dist
ARG BUILD_TARGET=dist
# ----------------------------------------------------------------------------------------------------------------------

# Base images
# ----------------------------------------------------------------------------------------------------------------------

FROM python:3.7 AS backend-base
###############################
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV="/data/venv"
WORKDIR /data
RUN pip install poetry==0.12.17 && python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY pyproject.toml poetry.lock ./
RUN poetry install
WORKDIR /data/mig3
COPY . ./

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FROM node:12.10-stretch AS frontend-base
########################################
WORKDIR /data/mig3-ui
COPY mig3-ui/package.json mig3-ui/yarn.lock ./
RUN yarn install
COPY mig3-ui ./

# ----------------------------------------------------------------------------------------------------------------------

# Development images
# ----------------------------------------------------------------------------------------------------------------------

FROM backend-base as backend-dev
################################
CMD ["/data/mig3/backend_dev_entrypoint.sh"]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FROM frontend-base AS frontend-dev
##################################
CMD ["yarn", "serve"]

# ----------------------------------------------------------------------------------------------------------------------

# Distribution image
# ----------------------------------------------------------------------------------------------------------------------

FROM frontend-base AS frontend-build
####################################
RUN yarn build

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FROM backend-base as dist
#########################
COPY --from=frontend-build /data/mig3-ui/dist /data/mig3/mig3-ui/dist
CMD ["make", "run"]

# ----------------------------------------------------------------------------------------------------------------------

# Finalized image
# ----------------------------------------------------------------------------------------------------------------------

FROM ${BUILD_TARGET} AS final
#############################
ARG BUILD_TARGET
LABEL com.github.mverteuil.mig3.build-target="${BUILD_TARGET}"
RUN echo "Finalized: ${BUILD_TARGET}"

# ----------------------------------------------------------------------------------------------------------------------
