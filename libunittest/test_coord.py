import unittest
from puzz import *

class TestCoord( unittest.TestCase):

	def test_const_get(self):

		c = Coord( 1, -2)
		self.assertEqual( c.get_row_no(), 1)
		self.assertEqual( c.get_col_no(), -2)

	def test_get_x_y( self):

		c = Coord( 1, -2)
		self.assertEqual( c.get_row_no(), c.get_y())
		self.assertEqual( c.get_col_no(), c.get_x())