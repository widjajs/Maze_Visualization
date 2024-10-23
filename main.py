import pygame
import sys
from utility_methods import update_display
from maze_generator import width, height, buffer, cream
from recursive_backtracker import recursive_backtrack
from prims_algorithm import prim_generate
from breadthfirst_search import bfs
from Astar_search import astar
from depthfirst_search import dfs
from dijkstra_search import dijkstra
from button import Button

pygame.init()
answered = False
screen = pygame.display.set_mode((600, 800))
screen.fill(cream)
pygame.display.flip()

# text disguised as buttons for convenience
generate_text = Button(0, 30, 600, 50, "Pick a Generation Algorithm!", 0)
solve_text = Button(0, 270, 600, 50, "Pick a Solving Algorithm!", 0)

generate_buttons = [
    Button(190, 100, 220, 50, "Prim's Algorithm", 0),
    Button(150, 170, 300, 50, "Recursive Backtracking", 1)
]
solving_buttons = [
    Button(210, 340, 180, 50, "A* Search", 0),
    Button(175, 410, 250, 50, "Depth-First Search", 1),
    Button(175, 480, 250, 50, "Dijkstra's Algorithm", 2),
    Button(175, 550, 250, 50, "Breadth-first Search", 3)
]
submit_button = Button(210, 670, 180, 50, "Submit", None)
generate_option = None
solving_option = None
gen_done = False
solve_done = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not answered:
            for button in generate_buttons:
                if button.is_clicked(event):
                    if not button.active:
                        for btn in generate_buttons:
                            btn.active = False
                        button.active = True
                        generate_option = button.button_id
                    else:
                        button.active = False
                        generate_option = None
            for button in solving_buttons:
                if button.is_clicked(event):
                    if not button.active:
                        for btn in solving_buttons:
                            btn.active = False
                        button.active = True
                        solving_option = button.button_id
                    else:
                        button.active = False
                        solving_option = None
            if submit_button.is_clicked(event) and generate_option is not None and solving_option is not None:
                answered = True

    if not answered:
        for button in generate_buttons:
            button.draw(screen, False)
        for button in solving_buttons:
            button.draw(screen, False);
        submit_button.draw(screen, False)
        generate_text.draw(screen, True)
        solve_text.draw(screen, True)
        update_display(0)

    if answered:
        if not gen_done and not solve_done:
            screen = pygame.display.set_mode((width + buffer, height + buffer))
            screen.fill(cream)

        # generate maze
        if not gen_done:
            if generate_option == 0:
                prim_generate()
            else:
                recursive_backtrack()
            gen_done = True

        # solve maze
        if not solve_done:
            if solving_option == 0:
                astar()
            elif solving_option == 1:
                dfs()
            elif solving_option == 2:
                dijkstra()
            else:
                bfs()
            solve_done = True

        update_display(0)
