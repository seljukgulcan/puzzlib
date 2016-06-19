import unittest
from puzzlib import *

class TestTile( unittest.TestCase):

	def test_const(self):

		t = Tile()
		self.assertEqual( t.get_value(), Tile.DEFAULT_VALUE)

		t = Tile(5)
		self.assertEqual( t.get_value(), 5)

	def test_set_get( self):

		t = Tile()
		t.set_value( 3)
		self.assertEqual( t.get_value(), 3)
		t.set_value( 4)
		self.assertEqual( t.get_value(), 4)