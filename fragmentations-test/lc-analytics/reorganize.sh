#!/bin/bash

FRAGS=('10' '50' '100' '300' '500' '1000' '3000' '5000' '10000' '20000' '30000')

mkdir $1
mkdir $1/datasets $1/linked_pages $1/stops
mkdir $1/datasets/min
cp min/datasets/$1/* $1/datasets/min
cp -r min/linked_pages/$1/ $1/linked_pages/min

for frag in ${FRAGS[*]}
  do
    if [[ $frag -ge $2 ]] && [[ $frag -le $3 ]]
    then
      mkdir $1/datasets/$frag
      mkdir $1/linked_pages/$frag
      mkdir $1/stops/$frag

      cp min/datasets/$1/* $1/datasets/$frag
      cp -r $frag/linked_pages/$1/* $1/linked_pages/$frag
    fi
  done