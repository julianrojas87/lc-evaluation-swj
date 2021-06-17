#!/bin/bash

echo "Name,%CPU"
while true; do
    docker stats --no-stream --format "{{.Name}},{{.CPUPerc}}"
done
