#!/usr/bin/env python3

import operator

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# Convert the dictionary to a list of tuples
scientists_list = [(key, value) for key, value in women_scientists.items()]

# Sort the list by date_of_birth using the operator.itemgetter function
sorted_scientists = sorted(scientists_list, key=lambda x: x[1]['date_of_birth'])

# Convert the sorted list back to a dictionary
sorted_women_scientists = dict(sorted_scientists)


def famous_births(people):
	for woman, dictionary in people.items():
		print(f"{dictionary['name']} is a great scientist born in {dictionary['date_of_birth']}.")

famous_births(sorted_women_scientists)