#!/usr/bin/env python3

people = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

def array_of_names(people):
	list = []
	for key, value in people.items():
		str = key.capitalize() + " " + value.capitalize()
		list.append(str)
	print(list)

array_of_names(people)