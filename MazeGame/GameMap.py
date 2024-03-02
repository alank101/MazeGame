from PIL import Image

maze_image1 = Image.open('Maze.png')

maze_image_grey1 = maze_image1.convert('L')

threshold = 128
maze_data = maze_image_grey1.point(lambda p: p > threshold and 1).load()

maze = []
for y in range(maze_image1.size[1]):
    row = []
    for x in range(maze_image1.size[0]):
        row.append(maze_data[x, y])
    maze.append(row)

print(maze[0])
# for row in maze:
#     print(row)