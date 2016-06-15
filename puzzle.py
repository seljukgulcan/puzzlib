from abc import ABCMeta, abstractmethod

class Puzzle(object):
	'''
		Shows general structure of a puzzle
	'''
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__( self):
		self._is_started = False
		self._is_over = False
		self._is_solved = False
	
	def is_over(self):
		return self._is_over
	
	def is_started( self):
		return self._is_started
	
	def is_solved( self):
		return self._is_solved
	
	def is_active( self):
		return self.is_started() and not self.is_over()