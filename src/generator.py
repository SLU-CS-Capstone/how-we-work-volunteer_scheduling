from maze import Maze
from sys import argv

size = 20
if (len(argv) > 1):
    size = int(argv[1])
maze = Maze(size)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")
