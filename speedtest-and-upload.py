#!/usr/bin/env python
"""Gathers results from speedtest-cli and uploads to Google Sheets"""
__author__ = "Adrian Campos"

import subprocess
import json
import requests

print('Fetching data from speedtest-cli...', end='', flush=True)

debug = False
if debug:
	# Use debug data
	json = json.loads('{"download": 40152439.07539318, "timestamp": "2017-01-26T01:19:43.616474", "ping": 29.283, "upload": 21166246.8474761, "server": {"latency": 29.283, "name": "Los Angeles, CA", "url": "http://losangeles-speedtest.atlanticmetro.net/speedtest/upload.php", "country": "United States", "lon": "-118.2500", "cc": "US", "host": "losangeles-speedtest.atlanticmetro.net:8080", "sponsor": "Atlantic Metro", "url2": "http://eng.lax0.atlanticmetro.net/speedtest/upload.php", "lat": "34.0500", "id": "2953", "d": 27.045541986010242}}')
else:
	# Load real data from speedtest-cli
	json = json.loads(subprocess.getoutput('/usr/local/bin/speedtest-cli --json'))
print('Done!')	

print('Sending to Google Sheets...', end='', flush=True)
# Send that data to Google Forms
# Form submit url
formurl = 'https://docs.google.com/forms/d/e/1FAIpQLSeTioT6eMpisW49rFx5q_g9LiJGgs8fT5YAPEe7YzDzqJxSMA/formResponse'

# Map json speedtest-cli's json keys to the Form's entry names
json_to_entryname = {
	'entry.886057421' : 'download',
	'entry.1384251079' : 'timestamp',
	'entry.100634473' : 'ping',
	'entry.1233962352' : 'upload'
}


data = {}
# Transfer json into data, replacing 'download' json key with 'entry.####' dictionary key
for entry in json_to_entryname:
	data[entry] = json[json_to_entryname[entry]]

# Append submit to the data so that it looks like a form request
data['submit'] = 'Submit'


# Send POST request to send data through Google Forms
requests.post(formurl, data=data)

print('Done!')
