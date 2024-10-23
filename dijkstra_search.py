import pygame
import sys
import heapq
from maze_generator import draw_maze, units, connect_path, slate_blue
from utility_methods import draw_path, get_valid_neighbors, update_display

def dijkstra():
    start = units[1][1]
    start.solved = True
    goal = units[len(units) - 2][len(units) - 2]
    distances = [[sys.maxsize for _ in range(len(units) - 2)] for _ in range(len(units) - 2)]
    distances[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, start))
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
            # path.reverse()
            draw_path(path)
            break

        for neighbor in get_valid_neighbors(current):
            neighbor.g = current.g + 1
            parent[neighbor] = current
            if neighbor.g < distances[neighbor.x - 1][neighbor.y - 1]:
                distances[neighbor.x - 1][neighbor.y - 1] = neighbor.g
                direction_priority = (neighbor.x, neighbor.y)
                heapq.heappush(queue, (neighbor.g, direction_priority, neighbor))

        draw_maze()
        update_display(0)

