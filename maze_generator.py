import pygame
import numpy as np

# colors
charcoal_gray = (51, 51, 51) # walls
muted_gold = (193, 165, 123) # generated visited
cream = (245, 245, 240) # background
slate_blue = (106, 90, 205) # solving visited
dusty_rose = (213, 166, 161) # path
powder_blue = (176, 224, 230)
sage_green = (158, 175, 143)
terracotta = (204, 132, 108)

# Configuration
buffer = 60  # Space between the grid and the screen edge
width, height = 800, 800  # Grid size (without buffer)
dimX, dimY = 40, 40
cell_width = width // dimX
cell_height = height // dimY

# Set up the display
screen = pygame.display.set_mode((width + buffer, height + buffer))
screen.fill(cream)
clock = pygame.time.Clock()

# Cell class representing walls on the right and bottom
class Cell:
    def __init__(self, x, y):
        self.right = True  # Wall on the right
        self.bottom = True  # Wall at the bottom
        self.visited = False  # Track if the cell is visited
        self.current = False
        self.solved = False
        self.path = False
        self.x = x
        self.y = y
        self.g = 0

# Create the grid with an invisible boundary (dimX + 2) x (dimY + 2)
units = [[Cell(row, col) for col in range(dimY + 2)] for row in range(dimX + 2)]
for i in range(dimX + 2):
    units[i][0].visited = True  # Left boundary
    units[i][dimY + 1].visited = True  # Right boundary
    units[i][0].solved = True  # Left boundary
    units[i][dimY + 1].solved = True  # Right boundary

for j in range(dimY + 2):
    units[0][j].visited = True  # Top boundary
    units[dimX + 1][j].visited = True  # Bottom boundary
    units[0][j].solved = True  # Top boundary
    units[dimX + 1][j].solved = True  # Bottom boundary

def draw_walls(x, y, cell):
    if cell.bottom:
        pygame.draw.line(screen, charcoal_gray, (x, y + cell_height), (x + cell_width, y + cell_height), 2)
    elif not cell.path and not cell.solved:  # make sure the background doesn't override solving path
        pygame.draw.line(screen, muted_gold, (x + 2, y + cell_height), (x + cell_width - 1, y + cell_height), 2)
    if cell.right:
        pygame.draw.line(screen, charcoal_gray, (x + cell_width, y), (x + cell_width, y + cell_height), 2)
    elif not cell.path and not cell.solved:  # make sure the background doesn't override solving path
        pygame.draw.line(screen, muted_gold, (x + cell_width, y + 2), (x + cell_width, y + cell_height - 1), 2)

def draw_maze():
    # Draw the inner grid walls
    for row in range(1, dimY + 1):
        for col in range(1, dimX + 1):
            x = (col - 1) * cell_width + buffer/2
            y = (row - 1) * cell_height + buffer/2
            if units[row][col].visited:
                pygame.draw.rect(screen, muted_gold, (x + 2, y + 2, cell_width - 2, cell_height - 2))
            if units[row][col].current:
                pygame.draw.rect(screen, slate_blue, (x + 2, y + 2, cell_width - 2, cell_height - 2))
            if units[row][col].solved:
                pygame.draw.rect(screen, slate_blue, (x + 2, y + 2, cell_width - 2, cell_height - 2))
            if units[row][col].path:
                pygame.draw.rect(screen, dusty_rose, (x + 2, y + 2, cell_width - 2, cell_height - 2))
            if row == 1 and col == 1:
                pygame.draw.rect(screen, sage_green, (x + 2, y + 2, cell_width - 2, cell_height - 2))
            if row == dimY and col == dimX:
                pygame.draw.rect(screen, terracotta, (x + 2, y + 2, cell_width - 2, cell_height - 2))
            draw_walls(x, y, units[row][col])

    # Draw the outer border of the grid
    pygame.draw.line(screen, charcoal_gray, (buffer/2, buffer/2), (width + buffer/2, buffer/2), 2)  # Top border
    pygame.draw.line(screen, charcoal_gray, (buffer/2, buffer/2), (buffer/2, height + buffer/2), 2)  # Left border



def connect_path(cell1, cell2, color):
    coords1 = np.array([cell1.x, cell1.y])
    coords2 = np.array([cell2.x, cell2.y])

    # Right/Down
    x1 = (cell1.y - 1) * cell_width + buffer/2
    y1 = (cell1.x - 1) * cell_height + buffer/2
    # Up/Left
    x2 = (cell2.y - 1) * cell_width + buffer/2
    y2 = (cell2.x - 1) * cell_height + buffer/2

    # connect paths
    if np.array_equal((coords2 - coords1), np.array([-1, 0])):  # Up
        pygame.draw.line(screen, color, (x2 + 2, y2 + cell_height), (x2 + cell_width, y2 + cell_height), 2)
    elif np.array_equal((coords2 - coords1), np.array([0, -1])):  # Left
        pygame.draw.line(screen, color, (x2 + cell_width, y2 + 2), (x2 + cell_width, y2 + cell_height - 1), 2)
    elif np.array_equal((coords2 - coords1), np.array([0, 1])):  # Right
        pygame.draw.line(screen, color, (x1 + cell_width, y1 + 2), (x1 + cell_width, y1 + cell_height - 1), 2)
    elif np.array_equal((coords2 - coords1), np.array([1, 0])):  # Down
        pygame.draw.line(screen, color, (x1 + 2, y1 + cell_height), (x1 + cell_width, y1 + cell_height), 2)


