#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]

print("[", end="")
for n in arr[:-1]:
	print(str(n), end=", ")
print(str(arr[-1]) + "]")