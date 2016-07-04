import types
from utils import _readline
import utils

class Grid(object):
	'''
		Representing a sqaure grid with particular number of rows and columns
	'''
	
	#CONSTRUCTORS
	def __init__( self, shape):
		self.__const_from_row_col( shape[0], shape[1])
	
	def __const_from_row_col( self, no_of_rows, no_of_cols):
		
		if( no_of_rows <= 0 or no_of_cols <= 0):
			raise ValueError("Grid constructor can only take positive values")

		self._grid = [[0 for j in range(no_of_cols)] for i in range(no_of_rows)]
		self._no_of_rows = no_of_rows
		self._no_of_cols = no_of_cols
	
	#PUBLIC METHODS
	def contains_pos( self, pos):
		if( pos[0] < 0 or pos[1] < 0):
			return False
		if( pos[0] >= self._no_of_rows or pos[1] >= self._no_of_cols):
			return False
		return True

	def get_shape( self):
		return ( self._no_of_rows, self._no_of_cols)

	def set_value( self, pos, value):
		
		self._grid[ pos[0]][ pos[1]] = value
	
	def get_value( self, pos):
		
		return self._grid[ pos[0]][ pos[1]]

	def save( self, filename = None, fd = None, close = True):
		fd = utils._get_file( "w", filename, fd)
		fd.write( str( self._no_of_rows) + " " + str( self._no_of_cols) + "\n")
		for i in self._grid:
			for j in i:
				fd.write( str( j))
				fd.write( " ")
			fd.write( "\n")
		if close:
			fd.close()

	@staticmethod
	def load( filename = None, fd = None, close = True):
		fd = utils._get_file( "r", filename, fd)
		size = None
		grid = None
		line_no = 0

		size = tuple( map( int, _readline( fd).split()))
		grid = Grid(size)

		for i in xrange( size[0]):
			row = map( int, _readline( fd).split())
			for j in xrange( len( row)):
				grid.set_value( ( i, j), row[j])

		#TODO: Remove code below if tests are successful
		'''
		for line in f:
			if( line[0] == "#"):
				continue
			if( size is None):
				size = tuple( map( int, line.split()))
				grid = Grid( size)
				continue
			row = map( int, line.split())
			for i in xrange( len( row)):
				grid.set_value( ( line_no, i), row[i])
			line_no += 1
		'''

		if close:
			fd.close()

		return grid

	def __str__(self):

		retVal = ""
		for i in self._grid:
			for j in i:
				retVal += str( j) + " "
			retVal += "\n"
		return retVal