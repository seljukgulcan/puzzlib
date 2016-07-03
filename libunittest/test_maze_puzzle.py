import unittest
from puzz import *

class TestMazePuzzle( unittest.TestCase):

	def test_const(self):

		p = MazePuzzle( (1, 2))
		self.assertEqual( p.get_shape(), (1,2))

	def test_set_start( self):

		p = MazePuzzle( (1, 2))
		p.set_start_position((0,1))
		self.assertEqual( (0,1), p.get_start_position())

	def test_set_finish( self):

		p = MazePuzzle( (1, 2))
		p.set_finish_position((0,1))
		self.assertEqual( (0,1), p.get_finish_position())

	def test_start( self):
		p = MazePuzzle( (1, 2))
		p.start();
		self.assertTrue( p.is_started())

	def test_move( self):
		p = MazePuzzle( (1, 2))
		p.start();
		p.move( Move.EAST)
		self.assertEqual( p.get_current_position(), (0,1))
		self.assertTrue( p.is_solved())

	def test_is_obstacle( self):
		p = MazePuzzle( (2,2))
		p.set_obstacles( [(0, 0)])

		self.assertTrue( p.is_obstacle( (0,0)))
		self.assertFalse( p.is_obstacle( (0,1)))
		self.assertFalse( p.is_obstacle( (1,0)))
		self.assertFalse( p.is_obstacle( (1,1)))

		p = MazePuzzle( (2,2))
		p.set_obstacles( [(0, 0), (0,1)])

		self.assertTrue( p.is_obstacle( (0,0)))
		self.assertTrue( p.is_obstacle( (0,1)))
		self.assertFalse( p.is_obstacle( (1,0)))
		self.assertFalse( p.is_obstacle( (1,1)))

		p = MazePuzzle( (2,2))
		p.set_obstacle( (1,1))

		self.assertFalse( p.is_obstacle( (0,0)))
		self.assertFalse( p.is_obstacle( (0,1)))
		self.assertFalse( p.is_obstacle( (1,0)))
		self.assertTrue( p.is_obstacle( (1,1)))