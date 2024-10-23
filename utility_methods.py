import pygame
import sys
from maze_generator import draw_maze, units, connect_path, dusty_rose


clock = pygame.time.Clock()

def draw_path(path):
    prev = path[0]
    prev.path = True
    for cell in path[1:]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        cell.path = True
        draw_maze()
        connect_path(prev, cell, dusty_rose)
        prev = cell
        update_display(100)

def get_valid_neighbors(cell):
    valid_neighbors = []
    if not cell.right and not (units[cell.x][cell.y + 1].solved):  # Right
        valid_neighbors.append(units[cell.x][cell.y + 1])
    if not cell.bottom and not (units[cell.x + 1][cell.y].solved):  # Down
        valid_neighbors.append(units[cell.x + 1][cell.y])
    if not units[cell.x - 1][cell.y].bottom and not (units[cell.x - 1][cell.y].solved):  # Up
        valid_neighbors.append(units[cell.x - 1][cell.y])
    if not units[cell.x][cell.y - 1].right and not (units[cell.x][cell.y - 1].solved): # Left
        valid_neighbors.append(units[cell.x][cell.y - 1])
    return valid_neighbors

def update_display(time):
    clock.tick(300)
    pygame.display.flip()
    pygame.time.delay(time)


