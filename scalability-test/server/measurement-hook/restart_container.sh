#!/bin/bash

sudo pkill -f recordstat
sudo docker container stop $(sudo docker ps -q)
sudo docker container prune
sudo docker run -p 8080:8080 --env-file=../conf.env --cpus=1 -d otp