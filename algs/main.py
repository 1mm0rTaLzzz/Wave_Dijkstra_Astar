import pygame
import numpy as np
import pandas as pd
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
                # dijkstra
                ordinal_number1 = x1 * 12 + y1
                ordinal_number2 = x * 12 + y
                print(ordinal_number1)
                adjacency_matrix = dijkstra_alg.get_adjacency_matrix(matrix)

                ordinal_number_of_path = dijkstra_alg.dijkstra(adjacency_matrix, ordinal_number2, ordinal_number1)
                path = list()
                for i in ordinal_number_of_path:
                    row_p, column_p = i // 12, i % 12
                    path.append([column_p, row_p])

                print(path)
                df = pd.DataFrame(adjacency_matrix)
                pd.set_option('display.max_rows', None)
                pd.set_option('display.max_columns', None)
                pd.set_option('display.width', None)
                print(df)
                for i in path[1:-1]:
                    grid[i[1]][i[0]] = GRAY
                # Wave
                '''
                way, matrix = solve(matrix, [x, y], [x1, y1])
                for i in way[:-1]:
                    grid[i[0]][i[1]] = GRAY
                '''
                end = time.time() - start
                print(end)

    screen.fill(WHITE)

    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(screen, grid[i][j], (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    pygame.display.update()

pygame.quit()
