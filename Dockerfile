FROM continuumio/miniconda3:latest AS build

LABEL maintainer="tkolleh <http://kolleh.com>"

COPY ./environment.yml /tmp/environment.yml

ARG CONDA_ENVNAME=pycrud-person

RUN conda env create --file /tmp/environment.yml
RUN conda install -c conda-forge conda-pack
RUN conda-pack -n $CONDA_ENVNAME -o /tmp/env.tar \ 
  && mkdir /venv \
  && cd /venv \
  && tar xf /tmp/env.tar \
  && rm /tmp/env.tar

RUN /venv/bin/conda-unpack

# Use Debian as the runtime-stage image. Everything else we need is apart of
# the pre-built conda env
FROM debian:buster AS runtime

COPY --from=build /venv /venv
COPY ./src /app/src
COPY ./config.ini /app/config.ini

ENV PYTHONPATH "/app:/app/src"

EXPOSE 8181/tcp

WORKDIR /app

SHELL ["/bin/bash", "-c"]
ENTRYPOINT source /venv/bin/activate \
  && python src/person_api/run.py
