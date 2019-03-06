#!/usr/bin/bash
for id in $(docker ps -aq); do
    echo $(docker exec $id jupyter notebook list)
done