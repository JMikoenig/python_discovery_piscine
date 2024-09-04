#!/usr/bin/env python3

import sys

count = 0
if len(sys.argv) != 2:
	print("none")
	exit()

for char in sys.argv[1]:
	if char == "z":
		count += 1
if count == 0:
	print("none")
else:
	print("z" * count)