#!/bin/bash

for dir in /users/jrojasme/lc-data/$1/datasets/*/; do # list directories
    dir=${dir%*/}      # remove the trailing "/"
    frag=${dir##*/}    # print everything after the final "/"
    node --max-old-space-size=12288 scripts/evaluation.js $1 $frag $2
   
done

