#!/bin/bash

i=0

for dir in /groups/ilabt-imec-be/openplanner/ptn-evaluation/fragmentations/*/; do # list directories
    ((i=i+1))
    if [[ i -gt $2 ]]
    then
        dir=${dir%*/}      # remove the trailing "/"
        ptn=${dir##*/}    # print everything after the final "/"
        node evaluation.js $ptn $1 1
    fi
done
