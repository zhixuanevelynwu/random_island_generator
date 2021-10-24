#! /usr/bin/env python3
''' Map visualization. '''
import pygame
import pygame.gfxdraw
from pygame.locals import *
import automaton


def main():
    pygame.init()
    width = 1034
    height = 778
    screen = pygame.display.set_mode([width, height])
    running = True
    grid_width = 12
    row = int(height / grid_width)
    col = int(width / grid_width)
    automata = automaton.Automata(col, row)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == K_q:  # Quit
                    running = False
                elif event.key == K_n:  # New
                    automata = automaton.Automata(col, row)
                elif event.key == K_f:  # Save to FILE
                    pygame.image.save(screen, 'automaton.png')
                elif event.key == K_a:  # Automaton
                    automata.life_stage(1)
                elif event.key == K_i:  # Automaton
                    automata.island_simulation(1, 4, 3)
                # create mountain (use after island is created completely)
                elif event.key == K_m:
                    automata.mountain_simulation(1, 4, 3)
                # create mountain (use after island and mountain are created completely)
                elif event.key == K_d:
                    automata.desert_simulation(1, 4, 3)
                elif event.key == K_s:  # fast generate:
                    # larger birthrate(second parameter) for less islands - default 4
                    B = 4
                    D = 3
                    automata.island_simulation(8, B, D)
                    automata.mountain_simulation(5, B, D)
                    automata.desert_simulation(5, B, D)
                    automata.island_simulation(1, B, D)
                    automata.mountain_simulation(3, B, D)
                    automata.desert_simulation(3, B, D)

        display_map(automata, screen, grid_width)
        pygame.display.flip()


def display_map(automata, screen, grid_width):
    island = pygame.Color('#8cc269')
    ocean = pygame.Color('#478de9')
    mountain = pygame.Color('#229453')
    desert = pygame.Color('#e3bd8d')
    screen.fill(ocean)
    for x in range(automata.row):
        for y in range(automata.col):
            c = automata.map[x][y]
            cell_x = x * grid_width + 5
            cell_y = y * grid_width + 5
            if c == 1:
                cell = pygame.Rect(cell_x, cell_y, grid_width, grid_width)
                pygame.draw.rect(screen, island, cell)
            if automata.mountain_map[x][y] == 1:
                cell = pygame.Rect(cell_x, cell_y, grid_width, grid_width)
                pygame.draw.rect(screen, mountain, cell)
            if automata.desert_map[x][y] == 1:
                cell = pygame.Rect(cell_x, cell_y, grid_width, grid_width)
                pygame.draw.rect(screen, desert, cell)


if __name__ == "__main__":
    main()
