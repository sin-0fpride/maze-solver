def solve_maze(maze, x, y, path):
    rows = len(maze)
    cols = len(maze[0])

    # Check if out of bounds or hitting a wall (1)
    if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] != 0:
        return False

    # Mark current cell as part of path
    path.append((x, y))

    # Mark the cell as visited
    maze[x][y] = 2

    # Check if it's the goal (bottom-right corner)
    if x == rows - 1 and y == cols - 1:
        return True

    # Try all 4 directions
    if (solve_maze(maze, x + 1, y, path) or 
        solve_maze(maze, x, y + 1, path) or 
        solve_maze(maze, x - 1, y, path) or 
        solve_maze(maze, x, y - 1, path)):
        return True

    # Backtrack: remove from path
    path.pop()
    return False

# Maze: 0 = path, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0]
]

path = []
if solve_maze(maze, 0, 0, path):
    print("Path found:")
    print(path)
else:
    print("No path found.")