#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
	exit()

for arg in sys.argv[1:]:
	if len(arg) >= 3 and arg[-3:] != "ism":
		print(f"{arg}ism")