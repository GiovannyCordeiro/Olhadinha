#!/bin/bash

l=$1

if [[ $l = "prod" || $l = "dev" ]] && [[ $2 = "down" || $2 = "up" ]]; then
    cd ..
    fileEnv="docker-compose.$l.yml"
    downOrUp=$2
    echo "Running docker-compose -f docker-compose.yml -f $fileEnv $downOrUp"
    docker-compose -f docker-compose.yml -f $fileEnv $downOrUp
else
    echo "Needed to follow format ./deploy.sh prod|dev down|up"
fi