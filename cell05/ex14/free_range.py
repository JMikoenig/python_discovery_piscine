#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("none")
	exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
list = [n for n in range(num1, num2)]

print(list)