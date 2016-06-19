from itertools import izip

def add_coord( a, b):
	return tuple(x + y for x, y in izip(a, b))