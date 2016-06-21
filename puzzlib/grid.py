import types
from tile import Tile
#from puzzlib import *

class Grid(object):
	'''
		Representing a sqaure grid with particular number of rows and columns
	'''
	
	#CONSTRUCTORS
	def __init__( self, *args):
		if( len(args) == 1 and type(args[0]) is tuple):
			self.__const_from_shape( args[0])
		elif( len(args) == 2 and type( args[0]) is int and type( args[1]) is int):
			self.__const_from_row_col( args[0], args[1])
		else:
			raise ValueError("Grid constructor can only take shape tuple or row-col pair")
	
	def __const_from_shape( self, shape):
		
		self.__const_from_row_col( shape[0], shape[1])
	
	def __const_from_row_col( self, no_of_rows, no_of_cols):
		
		if( no_of_rows <= 0 or no_of_cols <= 0):
			raise ValueError("Grid constructor can only take positive values")

		#self._grid = [[Tile()] * no_of_cols for i in xrange( no_of_rows)]
		self._grid = [[Tile() for j in range(no_of_cols)] for i in range(no_of_rows)]
		self._no_of_rows = no_of_rows
		self._no_of_cols = no_of_cols
	
	#PUBLIC METHODS
	def contains_pos( self, pos):
		if( pos[0] < 0 or pos[1] < 0):
			return False
		if( pos[0] >= self._no_of_rows or pos[1] >= self._no_of_cols):
			return False
		return True

	def set_value( self, pos, value):
		
		self._grid[ pos[0]][ pos[1]].set_value( value)
	
	def get_value( self, pos):
		
		return self._grid[ pos[0]][ pos[1]].get_value()

	def save( self, filename):
		f = open( filename, "w")
		f.write( str( self._no_of_rows) + " " + str( self._no_of_cols) + "\n")
		for i in self._grid:
			for j in i:
				f.write( str( j.get_value()) + " ")
			f.write( "\n")

	@staticmethod
	def load( filename):
		f = open( filename, "r")
		size = None
		grid = None
		line_no = 0
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

		return grid

	def __str__(self):

		retVal = ""
		for i in self._grid:
			for j in i:
				retVal += str( j.get_value()) + " "
			retVal += "\n"
		return retVal