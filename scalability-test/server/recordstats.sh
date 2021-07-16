#!/bin/bash

echo timestamp,name,%CPU,%Mem
while true; do
    LCS_STATS=$(docker stats --no-stream --format "{{.Name}},{{.CPUPerc}},{{.MemPerc}}" server_lc-server_1)
    NGINX_STATS=$(docker stats --no-stream --format "{{.Name}},{{.CPUPerc}},{{.MemPerc}}" server_nginx_1)
    DATE=`date +"%Y-%m-%dT%H:%M:%S"`
    echo $DATE,${LCS_STATS//%}
    echo $DATE,${NGINX_STATS//%}
done
