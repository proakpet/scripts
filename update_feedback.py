#!/usr/bin/env python3
import os, json
import requests

for file in os.listdir('/data/feedback/'):
	with open('/data/feedback/' + file) as f:
		dict = {}
		keys = ["title", "name", "date", "feedback"]
		for i in range(len(keys)):
			for line in f.readline().split('\n'):
				print(line)
				dict[keys[i]] = line
				response= requests.post('http://35.238.173.86//feedback/', json = dict)
				print(response.status_code)
