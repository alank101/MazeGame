# from PIL import Image

# maze_image1 = Image.open('Maze.png')

# maze_image_grey1 = maze_image1.convert('L')

# threshold = 128
# maze_data = maze_image_grey1.point(lambda p: p > threshold and 1).load()

# maze = []
# for y in range(maze_image1.size[1]):
#     row = []
#     for x in range(maze_image1.size[0]):
#         row.append(maze_data[x, y])
#     maze.append(row)

# print(maze[0])
# # for row in maze:
# #     print(row)

import random

def init_maze(width, height):
    # Initialize the maze grid with walls (1) and cells (0)
    maze = [[1 for _ in range(width)] for _ in range(height)]
    for x in range(1, height, 2):
        for y in range(1, width, 2):
            maze[x][y] = 0
    return maze

def carve_maze(x, y, maze):
    # Define the directions in which to carve
    dir = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(dir)  # Shuffle directions to ensure randomness
    
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 1 <= nx < len(maze)-1 and 1 <= ny < len(maze[0])-1 and maze[nx][ny] == 1:
            # Carve a path to the new cell
            maze[nx][ny] = 0
            maze[nx-dx//2][ny-dy//2] = 0  # Carve through the wall between cells
            carve_maze(nx, ny, maze)

def generate_maze(width, height):
    # Initialize maze with all walls
    maze = init_maze(width, height)
    
    # Randomly select a starting point with odd coordinates
    start_x, start_y = random.randrange(1, height, 2), random.randrange(1, width, 2)
    maze[start_x][start_y] = 0  # Set the starting cell as an empty path
    
    # Begin carving the maze from the starting point
    carve_maze(start_x, start_y, maze)
    
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(['#' if cell == 1 else ' ' for cell in row]))

# Example usage
width, height = 21, 21  # Maze dimensions (should be odd numbers)
maze = generate_maze(width, height)
print_maze(maze)