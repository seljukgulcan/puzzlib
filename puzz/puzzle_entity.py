from abc import ABCMeta, abstractmethod

class PuzzleEntity(object):
	'''
		Base class for all puzzlib entity classes which can be loaded from a file or saved to a file
	'''
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__( self):
		pass
	
	@staticmethod
	@abstractmethod
	def save( filepath = None, fd = None):
		if fd is None and filepath is None:
			raise ValueError('save method requires a valid parameter')

		if fd is None:
			pass

		return fd
	def _open_file( self, file_path, to_write = False):
		return self._is_over
	
	def _close_file( self, fd):
		return 