import types

class Grid(object):
	'''
		Representing a sqaure grid with particular number of rows and columns
	'''
	DEFAULT_VALUE = 0
	
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
		
		self._grid = [[Grid.DEFAULT_VALUE] * no_of_cols for i in xrange( no_of_rows)]
		self._no_of_rows = no_of_rows
		self._no_of_cols = no_of_cols
	
	#PUBLIC METHODS
	def set_value( self, value, row_no, col_no):
		
		self._grid[ row_no][ col_no] = value
	
	def get_value( self, row_no, col_no):
		
		return self._grid[ row_no][col_no]