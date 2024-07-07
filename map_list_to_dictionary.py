def map_dictionary(itr, fn):
    return dict(zip(itr, map(fn, itr)))


dd = map_dictionary([1, 2, 3], lambda x: 2 * x)
