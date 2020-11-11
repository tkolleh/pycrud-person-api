#!/bin/bash
set -euo pipefail

if [ -n "${1-}" ]; then
  docker run -d -p 8181:8181 "${1}"
else 
  TAG_ROOT="tkolleh"
  APPNAME="pycrud-person-api"
  IMAGE="${TAG_ROOT}/$APPNAME:latest"

  echo "======================================"
  echo "Setup & run application"
  echo ""
  echo "======================================"

  docker run -d $IMAGE
  sleep 3s
  echo ""
  docker ps
  echo ""
  echo "Visit http://localhost:8181 to access $APPNAME"
fi
