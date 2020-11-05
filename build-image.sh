#!/usr/bin/env bash

echo -e "Building project images"
TAG_ROOT="tkolleh"
APP_TAG="${TAG_ROOT}/pycrud-person-api:latest"

echo -e "Building app image"
docker build --file Dockerfile . -t $APP_TAG
