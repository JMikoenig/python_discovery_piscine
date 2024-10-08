#!/usr/bin/env python3

class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
}

class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13
}

def average(students):
	total = 0
	for student, mark in students.items():
		total += mark
	try:
		return (total / len(students))
	except ZeroDivisionError:
		print("No students, no average!")

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")