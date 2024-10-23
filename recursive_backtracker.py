import pygame
import sys
import random
from maze_generator import draw_maze, units
from utility_methods import update_display

def get_neighbors(cell):
    neighbors = []
    x, y = cell.x, cell.y
    if not units[x - 1][y].visited:  # up
        neighbors.append('U')
    if not units[x][y - 1].visited:  # left
        neighbors.append('L')
    if not units[x][y + 1].visited:  # right
        neighbors.append('R')
    if not units[x + 1][y].visited:  # down
        neighbors.append('D')

    return neighbors

def recursive_backtrack():
    stack = []
    current = units[1][1]
    current.visited = True
    current.current = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        neighbors = get_neighbors(current)

        # destory wall
        if neighbors:
            next = random.choice(neighbors)  # direction
            if next == 'U':
                units[current.x - 1][current.y].bottom = False
                next_cell = units[current.x - 1][current.y]
            elif next == 'L':
                units[current.x][current.y - 1].right = False
                next_cell = units[current.x][current.y - 1]
            elif next == 'D':
                current.bottom = False
                next_cell = units[current.x + 1][current.y]
            elif next == 'R':
                current.right = False
                next_cell = units[current.x][current.y + 1]

            stack.append(current)
            current.current = False
            current = next_cell
            current.visited = True
            current.current = True
        elif stack:
            current.current = False
            current = stack.pop()
            current.current = True
        else:
            break

        draw_maze()
        update_display(0)
    current.current = False
    draw_maze()
    update_display(0)
