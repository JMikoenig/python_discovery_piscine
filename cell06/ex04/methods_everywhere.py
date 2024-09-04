#!/usr/bin/env python3

import sys

zzz = "ZZZZZZZZ"

def shrink(str):
	print(str[:8])

def enlarge(str):
	print(str + zzz[:8 - len(arg)])

if len(sys.argv) == 1:
	print("none")

for arg in sys.argv[1:]:
	if len(arg) > 7:
		shrink(arg)
	else:
		enlarge(arg)