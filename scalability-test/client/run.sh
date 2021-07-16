#!/bin/bash

node --max-old-space-size=12288 ${SERVER}-scalability.js ${SERVER} ${SERVER_URI} ${SERVER_PORT} ${OPERATOR} \
    ${ITERATIONS} ${SUBSET} ${CONCURRENCIES} ${WORKERS} ${LOG} ${RECORD} ${AUTOCANNON}