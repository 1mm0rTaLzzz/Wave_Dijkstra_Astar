import pygame
import numpy as np
import wave_alg
import dijkstra_alg_v2
import Astar_alg
import RRT
import test

pygame.init()

win_size = (800, 800)

screen = pygame.display.set_mode(win_size)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
PURPLE = (139, 0, 250)
DARKBLUE = (0,33,55) #test
YELLOW = (255,255,0) #test

cell_size = 10

rows = win_size[1] // cell_size
cols = win_size[0] // cell_size

grid = np.array([[DARKBLUE for j in range(cols)] for i in range(rows)])

matrix = np.array([[0 for j in range(cols)] for i in range(rows)], dtype=np.float64)
print(np.size(matrix))
tree = np.array([], dtype=np.int64)
ways = np.array([], dtype=np.int16)

cr, cl = 0, 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            row = pos[1] // cell_size
            col = pos[0] // cell_size
            print(row, col)
            if event.button == 1:
                cl += 1
                if cl > 1:
                    grid[x][y] = DARKBLUE
                grid[row][col] = RED
                x, y = row, col
                matrix[row][col] = 0
                ways = ways.astype(np.int16)
                start = [x, y]
                for i in ways:
                    grid[i[0]][i[1]] = DARKBLUE
                ways = np.array([])
            elif event.button == 3:
                cr += 1
                if cr > 1:
                    grid[x1][y1] = DARKBLUE
                grid[row][col] = GREEN
                x1, y1 = row, col
                matrix[row][col] = 0
                ways = ways.astype(np.int16)
                for i in ways:
                    grid[i[0]][i[1]] = DARKBLUE
                ways = np.array([])
            elif event.button == 5 or event.button == 4:
                grid[row][col] = BLACK
                matrix[row][col] = -1
            '''
            elif event.button == 2:
                grid[row][col] = WHITE
                matrix[row][col] = 0
            '''
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
                ways = np.append(ways, np.array(way, dtype=np.int16).reshape(-1, 2))
                ways = ways.reshape(-1, 2)
                print(ways)
            elif event.key == pygame.K_SPACE:
                way, matrix1 = Astar_alg.solve(matrix, (x, y), (x1, y1))
                # way = test.astar((x, y), (x1, y1), matrix)
                for i in way[:-1]:
                    grid[i[0]][i[1]] = ORANGE
                # print(way)
                ways = np.append(ways, np.array(way, dtype=np.int16).reshape(-1, 2))
                ways = ways.reshape(-1, 2)
                print(ways)
            # RRT
            elif event.key == pygame.K_TAB:
                tree = np.insert(tree, 0, [x, y])
                for i in range(300):
                    len_edge, rs, newNode, tree, start = RRT.rrt(start, rows, cols, tree)
                    x2, y2 = start[0], start[1]
                    grid[newNode[0]][newNode[1]] = PURPLE
                    grid[x2][y2] = YELLOW

                    #RRT.root = RRT.Node([x,y])
                    #RRT.root.insert([x2, y2])
                    if RRT.dist([x2, y2], [x1, y1]) < RRT.re:
                        tree = np.append(tree, [x1, y1])
                        print("NASHEL!")
                        tree = tree.reshape(-1, 2).astype(np.int16)
                        break
                print(len(tree))
                grid[x][y] = RED
                #print(RRT.root.PreorderTraversal(RRT.root))
            elif event.key == pygame.K_0:
                for i in tree:
                    grid[i[0]][i[1]] = DARKBLUE
                    screen.fill(DARKBLUE)
                    #screen.fill(DARKBLUE)




    screen.fill(DARKBLUE)

    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(screen, grid[i][j], (j * cell_size, i * cell_size, cell_size, cell_size))
            # pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)
    #RRT
    for i in range(len(tree)):
        near_node = RRT.nearest_node(tree[i], tree, i)
        #print('jghgc',near_node)
        pygame.draw.aaline(screen, ORANGE,
                           [tree[i][1] * cell_size, tree[i][0] * cell_size],
                           [near_node[1] * cell_size, near_node[0] * cell_size])

    pygame.display.update()
    pygame.time.delay(10)
pygame.quit()
