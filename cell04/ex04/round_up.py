#!/usr/bin/env python3

try:
	num = float(input("Give me a number: "))
	print(round(num + 0.5))
except:
	print("Enter a valid number!")