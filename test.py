from puzzle import Puzzle
from grid import Grid
from maze_puzzle import MazePuzzle

grid = Grid( 5, 5)
grid.set_value( 5, 4, 2)
print ( grid.get_value( 4, 2))
print( "hi")

maze = MazePuzzle()