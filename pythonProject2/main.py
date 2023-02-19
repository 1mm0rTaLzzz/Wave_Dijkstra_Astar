import pygame
import numpy as np
import time
from wave_alg import solve
import dijkstra_alg


pygame.init()

win_size = (600, 600)

screen = pygame.display.set_mode(win_size)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

cell_size = 50

rows = win_size[1] // cell_size
cols = win_size[0] // cell_size

grid = np.array([[WHITE for j in range(cols)] for i in range(rows)])

matrix = np.array([[0 for j in range(cols)] for i in range(rows)])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            row = pos[1] // cell_size
            col = pos[0] // cell_size

            if event.button == 1:
                grid[row][col] = RED
                x, y = row, col
                matrix[row][col] = 0
            elif event.button == 3:
                grid[row][col] = GREEN
                x1, y1 = row, col
                matrix[row][col] = 0
            elif event.button == 2 or event.button == 5:
                grid[row][col] = BLACK
                matrix[row][col] = -1
            elif event.button == 5:
                grid[row][col] = WHITE
                matrix[row][col] = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = time.time()
                way, matrix = solve(matrix, [x1, y1], [x, y])
                '''
                matrix[matrix == -1] = 0
                print(matrix)
                dijkstra_alg.dijkstra(matrix, 0)
                '''
                for i in way[:-1]:
                    grid[i[0]][i[1]] = GRAY
                end = time.time() - start
                print(end)

    screen.fill(WHITE)

    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(screen, grid[i][j], (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    pygame.display.update()

pygame.quit()
