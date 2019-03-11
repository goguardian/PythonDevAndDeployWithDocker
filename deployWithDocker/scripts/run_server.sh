#!/usr/bin/env bash

# runs docker container  with Flask app and ML model
# best practice would be to use docker-compose up instead
# USAGE 
#

docker run \
    -p 8000:8000 \
    --rm \
    --name model_server_container \
    model_server:latest
