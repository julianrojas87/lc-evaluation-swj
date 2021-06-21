#!/bin/bash

sudo pkill -f recordstat
sudo docker rm $(sudo docker ps -a -q)
sudo docker run -p 8080:8080 --env-file=../conf.env --cpus=1 -d otp