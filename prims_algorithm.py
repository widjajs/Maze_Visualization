import pygame
import sys
import random
from maze_generator import draw_maze, units
from utility_methods import update_display

def get_walls(cell):
    valid_walls = []
    if cell.right and not (units[cell.x][cell.y + 1].visited):  # Right Wall
        valid_walls.append(((cell.x, cell.y), 'R'))
    if cell.bottom and not (units[cell.x + 1][cell.y].visited):  # Bottom Wall
        valid_walls.append(((cell.x, cell.y), 'B'))
    if units[cell.x - 1][cell.y].bottom and not (units[cell.x - 1][cell.y].visited):  # Top Wall
        valid_walls.append(((cell.x, cell.y), 'U'))
    if units[cell.x][cell.y - 1].right and not (units[cell.x][cell.y - 1].visited): # Left Wall
        valid_walls.append(((cell.x, cell.y), 'L'))
    return valid_walls

def prim_generate():
    walls = set()

    start = units[(int)(len(units)/2)][(int)(len(units)/2)]
    start.visited = True
    walls.update(get_walls(start))

    while walls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        next_wall = random.choice(list(walls))
        x, y = next_wall[0]
        direct = next_wall[1]

        if direct == 'R':
            if not (units[x][y + 1].visited):
                units[x][y].right = False
                units[x][y + 1].visited = True
                new_cell = units[x][y + 1]
        elif direct == 'B':
            if not (units[x + 1][y].visited):
                units[x][y].bottom = False
                units[x + 1][y].visited = True
                new_cell = units[x + 1][y]
        elif direct == 'L':
            if not (units[x][y - 1].visited):
                units[x][y - 1].right = False
                units[x][y - 1].visited = True
                new_cell = units[x][y - 1]
        elif direct == 'U':
            if not (units[x - 1][y].visited):
                units[x - 1][y].bottom = False
                units[x - 1][y].visited = True
                new_cell = units[x - 1][y]


        walls.update(get_walls(new_cell))

        walls.remove(next_wall)

        draw_maze()
        update_display(0)
