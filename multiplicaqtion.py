d1 = {'a': 2, 'b': 3, 'c': 4}
d2 = {'b': 5, 'c': 2, 'd': 6}

result = {}

for key in d1.keys() | d2.keys():
    result[key] = d1.get(key, 1) * d2.get(key, 1)

print(result)