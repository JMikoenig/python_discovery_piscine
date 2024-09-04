#!/usr/bin/env python3

try:
	num = int(input("Enter a number\n"))

	for n in range(10):
		print(f"{str(n)} x {str(num)} = {str(n * num)}")
except:
	print("Your input must be an integer")