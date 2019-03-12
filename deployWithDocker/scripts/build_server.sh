#!/usr/bin/env bash

# builds docker container  with Flask app and ML model
# best practice would be to use docker-compose build instead
# USAGE 
#

docker build -t model_server:latest ../docker
