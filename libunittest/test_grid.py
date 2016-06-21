import unittest
from puzzlib import *
import os

class TestGrid(unittest.TestCase):

	def test_create_grid( self):

		Grid( 3, 3)
		Grid( 1, 5)
		Grid( 5, 1)

		self.assertRaises( ValueError,  Grid, -3, 5)
		self.assertRaises( ValueError,  Grid, 5, -3)
		self.assertRaises( ValueError,  Grid, 0, 5)
		self.assertRaises( ValueError,  Grid, 5, 0)
		self.assertRaises( ValueError,  Grid, 0, 0)

	def test_set_get_grid_value( self):

		grid = Grid( 3, 5)

		grid.set_value( (1, 2), -8)
		grid.set_value( (2, 1), 4)
		grid.set_value( (0, 0), 5)

		self.assertEqual( grid.get_value( (1, 2)) , -8)
		self.assertEqual( grid.get_value( (2, 1)) , 4)
		self.assertEqual( grid.get_value( (0, 0)) , 5)

	def test_load_save( self):

		g = Grid( 2,3)

		for i in xrange( 2):
			for j in xrange( 3):
				g.set_value( (i, j), i + j)

		g.save( "test_load_save.tt")

		s = Grid.load( "test_load_save.tt")

		for i in xrange( 2):
			for j in xrange( 3):
				self.assertEqual( g.get_value( (i , j)), s.get_value( ( i, j)))

		os.remove( "test_load_save.tt")