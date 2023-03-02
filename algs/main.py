import pygame
import numpy as np
import wave_alg
import dijkstra_alg_v2
import Astar_alg


pygame.init()

win_size = (600, 600)

screen = pygame.display.set_mode(win_size)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)

cell_size = 50

rows = win_size[1] // cell_size
cols = win_size[0] // cell_size

grid = np.array([[WHITE for j in range(cols)] for i in range(rows)])

matrix = np.array([[0 for j in range(cols)] for i in range(rows)], dtype=np.float64)

ways=np.array([], dtype=np.int16)

cr,cl=0,0


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
                cl+=1
                if cl>1:
                    grid[x][y] = WHITE
                grid[row][col] = RED
                x, y = row, col
                matrix[row][col] = 0
                ways = ways.astype(np.int16)
                for i in ways:
                    grid[i[0]][i[1]]= WHITE
                ways = np.array([])
            elif event.button == 3:
                cr+=1
                if cr>1:
                    grid[x1][y1] = WHITE
                grid[row][col] = GREEN
                x1, y1 = row, col
                matrix[row][col] = 0
                ways = ways.astype(np.int16)
                for i in ways:
                    grid[i[0]][i[1]] = WHITE
                ways = np.array([])
            elif event.button == 2 or event.button == 5:
                grid[row][col] = BLACK
                matrix[row][col] = -1
            elif event.button == 5:
                grid[row][col] = WHITE
                matrix[row][col] = 0
            # Dijkstra
        elif event.type == pygame.KEYDOWN:
            matrix1 = matrix
            if event.key == pygame.K_LSHIFT:
                way, matrix1 = dijkstra_alg_v2.solve(matrix, [x, y], [x1, y1])
                for i in way[:-1]:
                    grid[i[0]][i[1]] = GRAY
                ways = np.append(ways, np.array(way, dtype=np.int16).reshape(-1, 2))
                ways = ways.reshape(-1, 2)
                print(ways)
            # Wave alg
            elif event.key == pygame.K_RSHIFT:
                way, matrix1 = wave_alg.solve(matrix, [x, y], [x1, y1])
                for i in way[:-1]:
                    grid[i[0]][i[1]] = BLUE
                ways = np.append(ways,np.array(way,dtype=np.int16).reshape(-1,2))
                ways = ways.reshape(-1, 2)
                print(ways)
            elif event.key == pygame.K_SPACE:
                way, matrix1 = Astar_alg.solve(matrix, (x, y), (x1, y1))
                #way = test.astar((x, y), (x1, y1), matrix)
                for i in way[:-1]:
                    grid[i[0]][i[1]] = ORANGE
                #print(way)
                ways = np.append(ways,np.array(way,dtype=np.int16).reshape(-1,2))
                ways = ways.reshape(-1, 2)
                print(ways)
    screen.fill(WHITE)

    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(screen, grid[i][j], (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    pygame.display.update()

pygame.quit()
