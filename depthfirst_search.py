import pygame
import sys
from collections import deque
from maze_generator import draw_maze, units, connect_path
from utility_methods import draw_path, get_valid_neighbors, update_display

def dfs():
    start = units[1][1]
    start.solved = True
    goal = units[len(units) - 2][len(units) - 2]
    queue = deque([start])
    parent = {start: None}


    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = queue.pop()
        if current == goal:
            path = []
            while not current is None:
                path.append(current)
                current = parent[current]
            # path.reverse()
            draw_path(path)
            break

        for neighbor in get_valid_neighbors(current):
            if neighbor not in parent:
                neighbor.solved = True
                connect_path(current, neighbor, (106, 90, 205))
                parent[neighbor] = current
                queue.append(neighbor)

        draw_maze()
        update_display(0)





