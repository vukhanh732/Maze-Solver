from collections import deque

def get_neighbors(maze, x, y):
    """
    Returns the valid neighbors of a cell in the given maze.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, down, left, up
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < maze.width and 0 <= ny < maze.height and not maze.maze[ny][nx].wall:
            neighbors.append((nx, ny))

    return neighbors

def solve_bfs(maze):
    """
    Solves the given maze using the Breadth-First Search algorithm.
    """
    queue = deque([(maze.start, [])])
    maze.maze[maze.start[1]][maze.start[0]].visited = True  # Visited

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == maze.end:
            yield path + [(x, y)]  # Found a path
            return

        for nx, ny in get_neighbors(maze, x, y):
            if not maze.maze[ny][nx].visited:  # Unvisited
                queue.append(((nx, ny), path + [(x, y)]))
                maze.maze[ny][nx].visited = True  # Mark as visited

        yield None  # Not yet found a path

    yield []  # No path found





