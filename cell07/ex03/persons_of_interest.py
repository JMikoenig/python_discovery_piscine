#!/usr/bin/env python3

import operator

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}


def famous_births(people):
	list = [(key, value) for key, value in women_scientists.items()]
	sorted_list = sorted(list, key = lambda x: x[1]['date_of_birth'])
	sorted_dict = dict(sorted_list)
	for woman, attributes in sorted_dict.items():
		print(f"{attributes['name']} is a great scientist born in {attributes['date_of_birth']}.")

famous_births(women_scientists)