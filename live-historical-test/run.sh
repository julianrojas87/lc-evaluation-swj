#!/bin/bash

# Start fake live data server
cd live-publish
node index.js &
cd ..
# Start LC-Server
cd lc-server
node bin/datasets &
node bin/web-server