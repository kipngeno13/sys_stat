#!/usr/bin/bash

#CPU usage

echo "======CPU Usage======"
mpstat

#Memory usage

echo "====Memory Usage===="
df -h 

#Network Statistics

echo "===Network Statistics==="

ss -s