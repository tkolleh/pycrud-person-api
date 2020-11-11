#!/usr/bin/env bash
set -euo pipefail

echo -e "\nBuilding project image(s)"
NAME_ROOT="tkolleh"
NAME="${NAME_ROOT}/pycrud-person-api"

echo -e "\nPull the latest version of the image to populate the build cache"
echo -e "\n****WARNING! comment out pull commands if there are docker registry errors****\n"
docker pull ${NAME}:build-stage || true
docker pull ${NAME}:latest || true
echo -e "\n****WARNING! comment out pull commands if there are docker registry errors****\n"

echo -e "\nBuild build-stage image..."
docker build --target build \
  --cache-from=${NAME}:build-stage \
  --tag ${NAME}:build-stage --file Dockerfile .

echo -e "\nBuild runtime image using cached build-stage image..."
docker build --target runtime \
  --cache-from=${NAME}:build-stage \
  --cache-from=${NAME}:latest \
  --tag ${NAME}:latest --file Dockerfile .

echo -e "\nPush the new image versions for all stages..."
docker push ${NAME}:build-stage
docker push ${NAME}:latest
