#!/usr/bin/env python3

import sys
import re

count = 0

if len(sys.argv) != 3:
	print("none")
	exit()

print(len(re.findall(sys.argv[1], sys.argv[2])))