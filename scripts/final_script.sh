#!/usr/bin/env bash

str2str -in "ntrip://sae:1234@10.0.0.6:2101/ARCT" >/dev/ttyS0 &
python "/home/pi/gps_testing/py_shi/src/Competition/echo-server.py"
pgrep -f str2str | xargs kill -9
