#!/usr/bin/env python3

input_num = input("Enter a number less than 25\n")
num = int(input_num)

if num > 25:
	print("Error")
	exit()

while num <= 25:
	print(f"Inside the loop, my variable is {str(num)}")
	num += 1