#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
cpy = set()

for n in arr:
	if n > 5:
		cpy.add(n + 2)

print(arr)
print(cpy)