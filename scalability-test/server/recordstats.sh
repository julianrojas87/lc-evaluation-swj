#!/bin/bash

echo timestamp,%CPU
while true; do
    CPU=$(docker stats --no-stream --format "{{.CPUPerc}}")
    DATE=`date +"%Y-%m-%dT%H:%M:%S"`
    echo $DATE,${CPU%?}
done
