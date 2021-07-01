#!/bin/bash

node --max-old-space-size=4096 ${SERVER}-scalability.js ${SERVER} ${SERVER_URI} ${SERVER_PORT} ${OPERATOR} \
    ${ITERATIONS} ${SUBSET} ${CONCURRENCIES} ${WORKERS} ${LOG} ${RECORD} ${AUTOCANNON}