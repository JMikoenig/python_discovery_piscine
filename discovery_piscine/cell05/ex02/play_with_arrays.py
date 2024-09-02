#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
cpy = []

for n in arr:
	if n > 5:
		cpy.append(n + 2)

print("Original array: [", end="")
for n in arr[:-1]:
	print(str(n), end=", ")
print(str(arr[-1]) + "]")

print("New array: [", end="")
for n in cpy[:-1]:
	print(str(n), end=", ")
print(str(cpy[-1]) + "]")