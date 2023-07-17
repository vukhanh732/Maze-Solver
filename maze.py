import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (200, 200, 0)
class Cell:
    def __init__(self):
        self.wall = False
        self.visited = False
        self.parent = None
        self.path = False  

class Maze:
    def __init__(self, cell_size, width, height):
        self.width = width // cell_size
        self.height = height // cell_size
        self.cell_size = cell_size
        self.maze = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.start = None
        self.end = None


    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                if self.maze[y][x].wall:  # Wall
                    pygame.draw.rect(screen, BLACK, rect)
                elif self.maze[y][x].path:  # Path
                    pygame.draw.rect(screen, YELLOW, rect)
                elif self.maze[y][x].visited:  # Visited
                    pygame.draw.rect(screen, GREEN, rect)
                else:  # Unvisited
                    pygame.draw.rect(screen, WHITE, rect)
        # draw the grid
        for x in range(0, self.width*self.cell_size, self.cell_size):
            pygame.draw.line(screen, BLACK, (x,0), (x,self.height*self.cell_size))
        for y in range(0, self.height*self.cell_size, self.cell_size):
            pygame.draw.line(screen, BLACK, (0,y), (self.width*self.cell_size,y))



