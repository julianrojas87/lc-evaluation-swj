#!/bin/bash

echo timestamp,name,%CPU,%Mem
while true; do
    LCS_STATS=$(docker stats --no-stream --format "{{.Name}},{{.CPUPerc}},{{.MemPerc}}")
    DATE=`date +"%Y-%m-%dT%H:%M:%S"`
    echo $DATE,${LCS_STATS//%}
done