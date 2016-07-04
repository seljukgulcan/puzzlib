from itertools import izip

def add( a, b):
	return tuple(x + y for x, y in izip(a, b))

def sub( a, b):
	return tuple(x - y for x, y in izip(a, b))

def _get_file( mode, filepath = None, fd = None):
	if fd is None and filepath is None:
		raise ValueError('_get_file function requires a valid file parameter')

	if fd is None:
		fd = open( filepath, mode)

	return fd

def _read_2tuple( fd):
	return tuple( map( int, _readline(fd).split()))

def _write_2tuple( fd, t):
	fd.write( str( t[0]) + " " + str( t[1]) + "\n")

def _readline( fd):

	line = "#"
	while line[0] == "#":
		line = fd.readline()

	return line