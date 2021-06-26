#!/bin/bash

# Replace environment variables with envsub
envsub datasets-config.json
# Start LC server
./bin/webserver