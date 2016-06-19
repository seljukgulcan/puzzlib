from puzzlib import *

maze = MazePuzzle( (3,3))

maze.set_obstacles( [(0,1), (1,1), (1,2)])
maze.set_start_position( (0,0))
maze.set_finish_position( (2,2))

maze.start()

print( "Maze game started")
while maze.is_active():

	print( maze)
	key = raw_input( "Move (wasd): ")
	print (key)
	move = None
	if( key == "w"):
		move = Move.NORTH

	elif( key == "s"):
		move = Move.SOUTH

	elif( key == "d"):
		move = Move.EAST

	elif( key == "a"):
		move = Move.WEST

	if move is not None:
		if maze.is_move_valid( move):
			maze.move( move)


print( "WON")