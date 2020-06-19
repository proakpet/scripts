#!/usr/bin/env python3
import re
import sys
"""
usage example:
>chmod +x check_cron.py
> ./check_cron.py syslog
[output]
"""

logfile = sys.argv[1]
with open(logfile) as f:
	for line in f:
		if "CRON" not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)
		print(result[1])