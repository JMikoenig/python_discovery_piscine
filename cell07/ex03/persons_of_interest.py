#!/usr/bin/env python3

import operator

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

scientists_list = [(key, value) for key, value in women_scientists.items()]
sorted_scientists = sorted(scientists_list, key = lambda x: x[1]['date_of_birth'])
sorted_women_scientists = dict(sorted_scientists)

def famous_births(people):
	for woman, attributes in people.items():
		print(f"{attributes['name']} is a great scientist born in {attributes['date_of_birth']}.")

famous_births(sorted_women_scientists)