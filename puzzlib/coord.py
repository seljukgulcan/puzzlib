class Coord(object):
	'''
		Represent a coordinate which can be used on a grid (or with other position related objects)
	'''
	
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
		__const_from_row_col( t[0], t[1])

	def __const_from_row_col( self, row_no, col_no):
		self.row_no = row_no
		self.col_no = col_no

	# PUBLIC METHODS
	def get_row_no( self):
		return self.row_no

	def get_col_no( self):
		return self.col_no

	def get_x( self):
		return self.get_col_no()

	def get_y( self):
		return self.get_row_no()