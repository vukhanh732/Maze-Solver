import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Maze:
    def __init__(self, cell_size, width, height):
        self.cell_size = cell_size
        self.width = width // cell_size
        self.height = height // cell_size
        self.maze = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def draw(self, screen):
        screen.fill(WHITE)
        for i in range(self.height):
            for j in range(self.width):
                x = j * self.cell_size
                y = i * self.cell_size
                if self.maze[i][j] == 1:
                    rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, BLACK, rect)
                else:
                    rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, WHITE, rect, 1)

    # Draw the grid
        for x in range(0, self.width*self.cell_size, self.cell_size):
            for y in range(0, self.height*self.cell_size, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, BLACK, rect, 1)