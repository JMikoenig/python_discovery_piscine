#!/usr/bin/env python3

import sys

if len(sys.argv) > 2:
	for n in reversed(sys.argv[1:]):
		print(n)
else:
	print("none")