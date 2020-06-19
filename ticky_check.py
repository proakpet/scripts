#!/usr/bin/env python3
import re
import operator
import csv, os, sys

error_message_count = {}
user_count = {}

with open("syslog.log", "r") as file:
	for line in file.readlines():
		pattern = re.search(r"(ERROR|INFO) (.*)\((.*)\)", line)
		msg_type = pattern.group(1)
		msg = pattern.group(2)
		uid = pattern.group(3)

		user_count[uid] = user_count.get(uid, {"ERROR": 0, "INFO":0})

		if msg_type == "ERROR":
			user_count[uid]["ERROR"] += 1
			error_message_count[msg] = error_message_count.get(msg,0)+1

		if msg_type == "INFO":
			user_count[uid]["INFO"] += 1

sorted_error_message_count = sorted(error_message_count.items(), key = operator.itemgetter(1), reverse = True)
sorted_user_count = sorted(user_count.items())

with open("error_message.csv", "w", newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Error", "Count"])
	writer.writerows(sorted_error_message_count)

with open("user_statistics.csv", "w", newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Username", "INFO", "ERROR"])

	for item in sorted_user_count:
		row = item[0], item[1]["INFO"], item[1]["ERROR"]
		writer.writerows(row)


"""
this program will create two csv files error_message.csv and user_statistics.csv
then convert csv to html and move it to var/www/html/
usage example:
>sudo ./csv_to_html.py error_message.csv /var/www/html/error.htm;
>sudo ./csv_to_html.py user_statistics.csv /var/www/html/user.html
"""
