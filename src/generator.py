from maze import Maze

maze = Maze(20)
maze.generate_maze()
choice = input("do you want in pdf(1) or terminal (2)")
if(choice == 1):
    maze.print(True)
if(choice==2):
    maze.print(False)

print("Welcome to 2D maze")
