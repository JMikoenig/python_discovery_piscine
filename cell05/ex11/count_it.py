#!/usr/bin/env python3

import sys

i = 0

if len(sys.argv) == 1:
	print("none")
	exit()

print(f"Parameters: {len(sys.argv) - 1}")
for arg in sys.argv[1:]:
	print(f"{arg}: {len(arg)}")