from puzzle import Puzzle
from tile import Tile
from grid import Grid
from move import Move
from utils import _readline
import utils
import os

class MazePuzzle( Puzzle):
	'''
		Maze puzzle
	'''

	OBSTACLE = 1
	OPEN = 0

	_DEFAULT_MOVES = set( [Move.NORTH, Move.EAST, Move.SOUTH, Move.WEST])
	
	# CONSRUCTOR
	def __init__( self, t):
		Puzzle.__init__(self)
		self._shape = t
		self._start_position = (0,0)
		self._finish_position = (t[0]-1, t[1]-1)
		self._grid = Grid( t)
		self._allowed_moves = MazePuzzle._DEFAULT_MOVES

	# PUBLIC METHODS
	def start( self):
		if( not self.is_active()):
			Puzzle.start( self)
		self._current_position = self._start_position

	def move( self, move):
		if( not self.is_active() or not self.is_move_valid( move)):
			return False

		new_pos = utils.add( self._current_position, move)
		self._current_position = new_pos

		if( self._current_position == self._finish_position):
			self._is_solved = True
			self._is_over = True

	def set_start_position( self, start):
		if( not self.is_active()):
			self._start_position = start

	def set_finish_position( self, finish):
		if( not self.is_active()):
			self._finish_position = finish

	def remove_obstacle( self, pos):
		self._grid.set_value( pos, OPEN)

	def remove_obstacles( self, pos_list):
		for pos in pos_list:
			self.remove_obstacle( pos)

	def set_obstacle( self, pos):
		self._grid.set_value( pos, MazePuzzle.OBSTACLE)

	def set_obstacles( self, pos_list):
		for pos in pos_list:
			self.set_obstacle( pos)

	def is_obstacle( self, pos):
		return self._grid.get_value( pos) == MazePuzzle.OBSTACLE

	def get_start_position( self):
		return self._start_position

	def get_finish_position( self):
		return self._finish_position

	def is_move_allowed( self, move):
		return move in _allowed_moves

	def is_move_valid( self, move):
		new_pos = utils.add( self._current_position, move)
		if( self._grid.contains_pos( new_pos)):
			if( not self.is_obstacle( new_pos)):
				return True
		return False

	def get_current_position( self):
		if( self.is_started()):
			return self._current_position
		return None

	def get_shape( self):
		return self._shape

	def get_allowed_moves( self):
		return self._allowed_moves

	def set_allowed_moves( self, moves):
		self._allowed_moves = moves

	def save( self, filepath=None, fd = None, close=True):

		fd = utils._get_file( "w", filepath, fd)

		utils._write_2tuple( fd, self._start_position)
		utils._write_2tuple( fd, self._finish_position)

		fd.write( str( len( self._allowed_moves)) + "\n")
		for i in self._allowed_moves:
			utils._write_2tuple( fd, i)

		self._grid.save( None, fd, False)

		if close:
			fd.close()

	@staticmethod
	def load( filepath = None, fd = None, close = True):
		fd = utils._get_file( "r", filepath, fd)

		start_pos = utils._read_2tuple( fd)
		finish_pos = utils._read_2tuple( fd)

		no_of_allowed_moves = int( utils._readline( fd))
		allowed_moves = set()
		for i in xrange( no_of_allowed_moves):
			allowed_moves.add( utils._read_2tuple( fd))

		grid = Grid.load( None, fd, False)

		puzzle = MazePuzzle( grid.get_shape())
		puzzle._grid = grid
		puzzle.set_allowed_moves( allowed_moves)
		puzzle.set_start_position( start_pos)
		puzzle.set_finish_position( finish_pos)

		if close:
			fd.close()

		return puzzle

	def __str__(self):

		retVal = "A Maze Game\n\n"

		if( self.is_active()):
			retVal += "Game is active\n"
			retVal += str( self.get_current_position()) + " <-- player location\n\n"

		retVal += str( self._grid)
		return retVal