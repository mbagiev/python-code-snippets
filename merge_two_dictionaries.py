dict_one = {'a': 1, 'b': 2, 'c': 3}
dict_two = {'d': 4, 'e': 5, 'f': 6}

# Method 1
result1 = {**dict_one, **dict_two}

# Method 2
result2 = dict_one.copy()
result2.update(dict_two)

# Method 3
result3 = {key: value for d in (dict_one, dict_two) for key, value in d.items()}
