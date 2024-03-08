#!/usr/bin/env bash

nohup str2str -in "ntrip://sae:1234@10.0.0.2:2101/ARCT" >/dev/ttyS0 &
python "/home/pi/gps_testing/py_shi/src/Competition/echo-server.py"
pgrep -f str2str | xargs kill -9
