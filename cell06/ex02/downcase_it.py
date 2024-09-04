#!/usr/bin/env python3

import sys

def downcase_it(str):
	print(str.lower())

if len(sys.argv) < 2:
	print("none")
	exit()

for arg in sys.argv:
	downcase_it(arg)