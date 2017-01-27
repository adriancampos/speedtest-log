#!/bin/bash

# Old method of logging:
# date >> /home/pi/speedtest-log/speedtest.log
# /usr/local/bin/speedtest --simple >> /home/pi/speedtest-log/speedtest.log

# Log with Google Sheets:
python3 /home/pi/speedtest-log/speedtest-and-upload.py


