from puzzlib import *

class Move(object):
	'''
		This class represents a move in term of directions
	'''

	#NORTH = None
	
	# CONSTRUCTORS
	def __init__( self, *args):
		if( len(args) == 0):
			__init__( (0, 0))
		if( len(args) == 1 and type(args[0]) is tuple):
			self.__const_from_tuple( args[0])
		elif( len(args) == 2 and type( args[0]) is int and type( args[1]) is int):
			self.__const_from_row_col( args[0], args[1])
		else:
			raise ValueError("Coord constructor can only take pair-tuple or row-col pair")

	def __const_from_tuple( self, t):
		self.__const_from_row_col( t[0], t[1])

	def __const_from_row_col( self, row_no, col_no):
		self.row_move = row_no
		self.col_move = col_no

	# PUBLIC METHODS
	def get_row_move( self):
		return self.row_move

	def get_col_move( self):
		return self.col_move

# CONSTANTS
Move.NORTH = Move( -1, 0)
Move.SOUTH = Move( 1, 0)
Move.EAST = Move( 0, 1)
Move.WEST = Move( 0, -1)