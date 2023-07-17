import pygame
from maze import Maze

# Pygame configuration
WIDTH, HEIGHT = 800, 800  # Window dimensions
FPS = 60  # Frames per second

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# Initialize Maze
maze = Maze(20, WIDTH, HEIGHT)  # 20 is the size of a cell in the grid

# Game loop
running = True
while running:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the reset button
    button_color = (0, 200, 0)  # Green color
    button_rect = pygame.Rect(10, 10, 100, 50)  # Button position and size
    pygame.draw.rect(SCREEN, button_color, button_rect)
    
    # Draw the text on the button
    font = pygame.font.Font(None, 24)  # Use the default font and size 24
    text = font.render('Reset', True, (0, 0, 0))  # Black color
    SCREEN.blit(text, (button_rect.x + 20, button_rect.y + 15))  # Position the text
                
    # Check if the left mouse button is pressed
    if pygame.mouse.get_pressed()[0]:
        # Get the mouse position
        mx, my = pygame.mouse.get_pos()
        # Convert the mouse position to grid coordinates
        gx, gy = mx // 20, my // 20
        # Change the corresponding cell in the maze to a wall
        maze.maze[gy][gx] = 1


    maze.draw(SCREEN)

    pygame.display.flip()  # Update the screen

pygame.quit()
