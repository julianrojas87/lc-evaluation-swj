#!/bin/bash

for dir in /groups/ilabt-imec-be/openplanner/ptn-evaluation/fragmentations/*/; do # list directories
    dir=${dir%*/}      # remove the trailing "/"
    ptn=${dir##*/}    # print everything after the final "/"
    node evaluation.js $ptn $1 5
done

