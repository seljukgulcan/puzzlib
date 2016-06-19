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

	def __str__(self):

		retVal = ""
		for i in self._grid:
			for j in i:
				retVal += str( j.get_value()) + " "
			retVal += "\n"
		return retVal