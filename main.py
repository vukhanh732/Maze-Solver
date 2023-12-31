import pygame
from maze import Maze
from algorithm import solve_bfs, solve_dfs, solve_dijkstra
# Pygame configuration
WIDTH, HEIGHT = 850, 850  # Window dimensions
MAZE_WIDTH, MAZE_HEIGHT = 700, 700  # Maze dimensions
FPS = 60  # Frames per second
no_path_message = ""  # Message to display when no path is found

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)

# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# Initialize Maze
maze = Maze(20, MAZE_WIDTH, MAZE_HEIGHT)  # 20 is the size of a cell in the grid
placing_start = False
placing_end = False

# Initialize BFS button
bfs_button_color = (200, 0, 0)  # Red color
bfs_button_rect = pygame.Rect(701, 60, 100, 50)  # Button position and size
bfs_generator = None

# Initialize DFS button
dfs_button_color = (200, 0, 0)  # Red color
dfs_button_rect = pygame.Rect(701, 120, 100, 50)  # Button position and size
dfs_generator = None

# Initialize Dijkstra button
dijkstra_button_color = (200, 0, 0)  # Red color
dijkstra_button_rect = pygame.Rect(701, 180, 100, 50)  # Button position and size
dijkstra_generator = None

# Game loop
running = True
while running:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            # Check if the reset button was clicked
            if pygame.Rect(701, 0, 100, 50).collidepoint(event.pos):
                maze = Maze(20, MAZE_WIDTH, MAZE_HEIGHT)  # Create a new empty maze
                placing_start = False
                placing_end = False
                bfs_generator = None  # Clear the BFS generator
                dfs_generator = None  # Clear the DFS generator
                dijkstra_generator = None  # Clear the Dijkstra generator
                no_path_message = "" # Clear the no path message

            # Check if the BFS button was clicked
            elif bfs_button_rect.collidepoint(event.pos):
                bfs_generator = solve_bfs(maze)  # Start the BFS algorithm
            # Check if the DFS button was clicked
            elif dfs_button_rect.collidepoint(event.pos):
                dfs_generator = solve_dfs(maze)  # Start the DFS algorithm
            # Check if the Dijkstra button was clicked
            elif dijkstra_button_rect.collidepoint(event.pos):
                dijkstra_generator = solve_dijkstra(maze)  # Start Dijkstra's algorithm

            # If mouse is outside the maze, ignore the click    
            else:
                # Convert the mouse position to grid coordinates
                gx, gy = mx // 20, my // 20
                # Check if we are in placing start mode
                if placing_start and gx < maze.width and gy < maze.height:
                    maze.start = (gx, gy)
                    placing_start = False
                # Check if we are in placing end mode
                elif placing_end and gx < maze.width and gy < maze.height:
                    maze.end = (gx, gy)
                    placing_end = False
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                placing_start = True
            elif event.key == pygame.K_e:
                placing_end = True

    # Check if the left mouse button is being held down
    if pygame.mouse.get_pressed()[0] and not (placing_start or placing_end):
        # Get the mouse position
        mx, my = pygame.mouse.get_pos()
        # Convert the mouse position to grid coordinates
        gx, gy = mx // 20, my // 20
        # Check if the click is within the grid
        if gx < maze.width and gy < maze.height:
            # Change the corresponding cell in the maze to a wall
            if maze.start != (gx, gy) and maze.end != (gx, gy):
                maze.maze[gy][gx].wall = True  # set wall attribute to True

    # Advance the BFS algorithm by one step and redraw the maze
    if bfs_generator is not None:
        try:
            next(bfs_generator)
        except StopIteration:
            bfs_generator = None  # BFS has finished running
    # Advance the DFS algorithm by one step and redraw the maze
    if dfs_generator is not None:
        try:
            next(dfs_generator)
        except StopIteration:
            dfs_generator = None  # DFS has finished running
    # Advance the Dijkstra algorithm by one step and redraw the maze
    if dijkstra_generator is not None:
        try:
            next(dijkstra_generator)
        except StopIteration:
            dijkstra_generator = None  # Dijkstra has finished running


    maze.draw(SCREEN)

    # Draw the reset button
    button_color = (0, 200, 0)  # Green color
    button_rect = pygame.Rect(701, 0, 100, 50)  # Button position and size
    pygame.draw.rect(SCREEN, button_color, button_rect)

    # Draw the text on the button
    font = pygame.font.Font(None, 24)  # Use the default font and size 24
    text = font.render('Reset', True, (0, 0, 0))  # Black color
    SCREEN.blit(text, (button_rect.x + 20, button_rect.y + 15))  # Position the text

    # Draw the start and end points
    if maze.start:
        pygame.draw.circle(SCREEN, RED, (maze.start[0]*20+10, maze.start[1]*20+10), 10)
    if maze.end:
        pygame.draw.circle(SCREEN, BLUE, (maze.end[0]*20+10, maze.end[1]*20+10), 10)

    # Draw the BFS button
    pygame.draw.rect(SCREEN, bfs_button_color, bfs_button_rect)
    text = font.render('BFS', True, (0, 0, 0))  # Black color
    SCREEN.blit(text, (bfs_button_rect.x + 35, bfs_button_rect.y + 15))  # Position the text

    # Draw the BFS button
    pygame.draw.rect(SCREEN, bfs_button_color, bfs_button_rect)
    text = font.render('BFS', True, (0, 0, 0))  # Black color
    SCREEN.blit(text, (bfs_button_rect.x + 35, bfs_button_rect.y + 15))  # Position the text

    # Draw the DFS button
    pygame.draw.rect(SCREEN, dfs_button_color, dfs_button_rect)
    text = font.render('DFS', True, (0, 0, 0))  # Black color
    SCREEN.blit(text, (dfs_button_rect.x + 35, dfs_button_rect.y + 15))  # Position the text

    # Draw the Dijkstra button
    pygame.draw.rect(SCREEN, dijkstra_button_color, dijkstra_button_rect)
    text = font.render('Dijkstra', True, (0, 0, 0))  # Black color
    SCREEN.blit(text, (dijkstra_button_rect.x + 25, dijkstra_button_rect.y + 15))  # Position the text

    # Draw the no path message
    if no_path_message:
        font = pygame.font.Font(None, 36)
        text = font.render(no_path_message, True, RED)
        SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()  # Update the screen

pygame.quit()
