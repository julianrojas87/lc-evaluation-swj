#!/bin/bash

echo "Container,Name,%CPU,Memory-Usage,%Memory,Net-IO"
while true; do
    docker stats --no-stream --format "{{.Container}},{{.Name}},{{.CPUPerc}},{{.MemUsage}},{{.MemPerc}},{{.NetIO}}"
done
