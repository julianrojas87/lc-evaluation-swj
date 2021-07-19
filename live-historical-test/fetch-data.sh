#!/bin/bash

while true
do
    NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    gtfsrt2json -r https://sncb-opendata.hafas.de/gtfs/realtime/c21ac6758dd25af84cca5b707f3cb3de > ${NOW}.json
    sleep 30
done