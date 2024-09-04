#!/usr/bin/env python3

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

def find_the_redheads(people):
	list = []
	for key, value in people.items():
		if value == "red":
			list.append(key)
	print(list)

find_the_redheads(dupont_family)