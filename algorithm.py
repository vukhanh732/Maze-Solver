from collections import deque
import heapq

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
    queue = deque([maze.start])
    found = False 

    while queue:
        x, y = queue.popleft()

        if (x, y) == maze.end:
            found = True 
            break  

        for nx, ny in get_neighbors(maze, x, y):
            if not maze.maze[ny][nx].visited:  # Unvisited
                queue.append((nx, ny))
                maze.maze[ny][nx].visited = True  # Mark as visited
                maze.maze[ny][nx].parent = x, y

        yield False  # Not yet found a path

    # If a path is found, trace the path
    if found:
        x, y = maze.end
        while (x, y) != maze.start:
            maze.maze[y][x].path = True
            x, y = maze.maze[y][x].parent
        maze.maze[maze.start[1]][maze.start[0]].path = True

    yield found


def solve_dfs(maze):
    """
    Solves the given maze using the Depth-First Search algorithm.
    """
    stack = [maze.start]
    found = False 

    while stack:
        x, y = stack.pop()

        if (x, y) == maze.end:
            found = True 
            break  

        for nx, ny in get_neighbors(maze, x, y):
            if not maze.maze[ny][nx].visited:  # Unvisited
                stack.append((nx, ny))
                maze.maze[ny][nx].visited = True  # Mark as visited
                maze.maze[ny][nx].parent = x, y

        yield False  # Not yet found a path

    # If a path is found, trace the path
    if found:
        x, y = maze.end
        while (x, y) != maze.start:
            maze.maze[y][x].path = True
            x, y = maze.maze[y][x].parent
        maze.maze[maze.start[1]][maze.start[0]].path = True

    yield found

def solve_dijkstra(maze):
    """
    Solves the given maze using Dijkstra's algorithm.
    """
    queue = [(0, maze.start)]
    distances = {maze.start: 0}
    found = False 

    while queue:
        dist, (x, y) = heapq.heappop(queue)

        if (x, y) == maze.end:
            found = True 
            break  

        for nx, ny in get_neighbors(maze, x, y):
            new_dist = dist + 1  # All edges have weight 1
            if not maze.maze[ny][nx].visited or new_dist < distances[(nx, ny)]:  # Unvisited or shorter path
                distances[(nx, ny)] = new_dist
                heapq.heappush(queue, (new_dist, (nx, ny)))
                maze.maze[ny][nx].visited = True  # Mark as visited
                maze.maze[ny][nx].parent = x, y

        yield False  # Not yet found a path

    # If a path is found, trace the path
    if found:
        x, y = maze.end
        while (x, y) != maze.start:
            maze.maze[y][x].path = True
            x, y = maze.maze[y][x].parent
        maze.maze[maze.start[1]][maze.start[0]].path = True

    yield found
