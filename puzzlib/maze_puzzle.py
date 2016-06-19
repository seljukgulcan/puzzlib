from puzzle import Puzzle
from tile import Tile
from grid import Grid
from utils import *

class MazePuzzle( Puzzle):
	'''
		Maze puzzle
	'''

	OBSTACLE = 1
	OPEN = Tile.DEFAULT_VALUE
	
	# CONSRUCTOR
	def __init__( self, *args):
		Puzzle.__init__( self)
		if( len(args) == 1 and type(args[0]) is tuple):
			self.__const_from_tuple( args[0])
		elif( len(args) == 2 and type( args[0]) is int and type( args[1]) is int):
			self.__const_from_row_col( args[0], args[1])
		else:
			raise ValueError("MazePuzzle constructor can only take pair-tuple or row-col pair")

	def __const_from_tuple( self, t):
		self.__shape = t
		self.__start_position = (0,0)
		self.__finish_position = (t[0]-1, t[1]-1)
		self.__grid = Grid( t)

	def __const_from_row_col( self, row_no, col_no):
		self.__const_from_tuple( (row_no, col_no))

	# PUBLIC METHODS
	def start( self):
		if( not self.is_active()):
			Puzzle.start( self)
		self.__current_position = self.__start_position

	def move( self, move):
		if( not self.is_active() or not self.is_move_valid( move)):
			return False

		new_pos = add_coord( self.__current_position, (move.get_row_move(), move.get_col_move()))
		self.__current_position = new_pos

		if( self.__current_position == self.__finish_position):
			self._is_solved = True
			self._is_over = True

	def set_start_position( self, start):
		if( not self.is_active()):
			self.__start_position = start

	def set_finish_position( self, finish):
		if( not self.is_active()):
			self.__finish_position = finish

	def remove_obstacle( self, pos):
		self.__grid.set_value( pos, OPEN)

	def remove_obstacles( self, pos_list):
		for pos in pos_list:
			self.remove_obstacle( pos)

	def set_obstacle( self, pos):
		self.__grid.set_value( pos, MazePuzzle.OBSTACLE)

	def set_obstacles( self, pos_list):
		for pos in pos_list:
			self.set_obstacle( pos)

	def is_obstacle( self, pos):
		return self.__grid.get_value( pos) == MazePuzzle.OBSTACLE

	def get_start_position( self):
		return self.__start_position

	def get_finish_position( self):
		return self.__finish_position

	def is_move_allowed( self, move):
		return True

	def is_move_valid( self, move):
		new_pos = add_coord( self.__current_position, (move.get_row_move(), move.get_col_move()))
		if( self.__grid.contains_pos( new_pos)):
			if( not self.is_obstacle( new_pos)):
				return True
		return False

	def get_current_position( self):
		if( self.is_started()):
			return self.__current_position
		return None

	def get_shape( self):
		return self.__shape

	def __str__(self):

		retVal = "A Maze Game\n\n"

		if( self.is_active()):
			retVal += "Game is active\n"
			retVal += str( self.get_current_position()) + " <-- player location\n\n"

		retVal += str( self.__grid)
		return retVal