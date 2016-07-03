from itertools import izip

def add( a, b):
	return tuple(x + y for x, y in izip(a, b))

def sub( a, b):
	return tuple(x - y for x, y in izip(a, b))