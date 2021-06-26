#!/bin/bash

# Replace environment variables with envsub
envsub datasets_config.json
# Start LC server
./bin/web-server