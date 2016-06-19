import unittest
from puzzlib import *

class TestMove( unittest.TestCase):

	def test_const_get(self):

		t = Move( 1, 2)
		self.assertEqual( t.get_row_move(), 1)
		self.assertEqual( t.get_col_move(), 2)

		t = Move( (1, 2))
		self.assertEqual( t.get_row_move(), 1)
		self.assertEqual( t.get_col_move(), 2)