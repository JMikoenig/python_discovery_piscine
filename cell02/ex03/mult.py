#!/usr/bin/env python3

num1 = input("Enter the first number: \n")
num2 = input("Enter the second number: \n")

print(f"{num1} x {num2} = {int(num1) * int(num2)}")
if int(num1) * int(num2) < 0:
	print("This number is negative.")
if int(num1) * int(num2) > 0:
	print("This number is positive.")
if int(num1) * int(num2) == 0:
	print("This number is positive and negative.")