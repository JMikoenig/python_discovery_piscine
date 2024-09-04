#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
	print("none")
	exit()

row = 0
col = 0

while row <= 10:
	table = "Table de " + str(row) + ": "
	col = 0
	while col <= 10:
		table += str(row * col) + " "
		col += 1
	print(table)
	row += 1