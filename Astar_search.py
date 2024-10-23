import pygame
import sys
import heapq
from maze_generator import draw_maze, units, connect_path, slate_blue
from utility_methods import get_valid_neighbors, draw_path, update_display

def get_dist(start, end):
    return abs(start.x - end.x) + abs(start.y - end.y)

def astar():
    start = units[1][1]
    start.solved = True
    goal = units[len(units) - 2][len(units) - 2]
    queue = []
    heapq.heappush(queue, (get_dist(start, goal) + start.g, start))
    parent = {start: None}

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        current = heapq.heappop(queue)[-1]
        current.solved = True
        if current in parent and parent[current] is not None:
            connect_path(parent[current], current, slate_blue)

        if current == goal:
            path = []
            while not current is None:
                path.append(current)
                current = parent[current]
            path.reverse()
            draw_path(path)
            break

        for neighbor in get_valid_neighbors(current):
            if neighbor.solved:
                continue
            if neighbor not in parent or current.g + 1 < neighbor.g:
                neighbor.g = current.g + 1
                parent[neighbor] = current
                direction_priority = (neighbor.x, neighbor.y)
                heapq.heappush(queue, (neighbor.g + get_dist(neighbor, goal), direction_priority, neighbor))

        draw_maze()
        update_display(0)




