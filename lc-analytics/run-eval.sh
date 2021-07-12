#!/bin/bash

i=0

for dir in /users/jrojasme/lc-data/$1/datasets/*/; do # list directories
    ((i=i+1))
    if [[ i -gt $2 ]]
    then
        dir=${dir%*/}      # remove the trailing "/"
        ptn=${dir##*/}    # print everything after the final "/"
        node --max-old-space-size=8092 scripts/evaluation.js $ptn $1 1
    fi
done

