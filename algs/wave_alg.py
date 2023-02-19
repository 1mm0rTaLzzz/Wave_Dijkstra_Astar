import numpy as np


def solve(matrix, start, end):
    wavefront = np.array([[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))])
    wavefront[start[0]][start[1]] = 1

    wave_value = 1
    check = 0
    while wavefront[end[0]][end[1]] == -1 and check <= 200:
        check += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if wavefront[i][j] == wave_value:
                    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1),
                                 (i - 1, j + 1), (i + 1, j - 1)]
                    for neighbor in neighbors:
                        if neighbor[0] >= 0 and neighbor[0] < len(matrix) and neighbor[1] >= 0 and neighbor[1] < len(
                                matrix[0]):
                            if wavefront[neighbor[0]][neighbor[1]] == -1 and matrix[neighbor[0]][neighbor[1]] == 0:
                                wavefront[neighbor[0]][neighbor[1]] = wave_value + 1
        wave_value += 1
    matrix = wavefront
    print(matrix)

    way = np.array([[], []])
    move = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]])  # 8 move ver
    # move = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]]) # 4 move ver
    print('Point start', start, '\n', 'Point end', end)
    temp_x, temp_y = end[0], end[1]
    temp = matrix[temp_x][temp_y] - 1
    while temp != 0:
        count = 0
        if temp < 1:
            print('Нет пути')
            break

        for m in move:
            step_x = temp_x + m[0]
            step_y = temp_y + m[1]
            try:
                if matrix[step_x, step_y] == temp:
                    way = np.append(way, np.array([step_x, step_y]))
                    temp_x, temp_y = step_x, step_y
                    temp = matrix[temp_x][temp_y] - 1
                    break
                else:
                    count = count + 1
            except Exception:
                print('Something goes wrong :D')

    way = way.astype(np.int16)
    way = way.reshape(-1, 2)
    return way, matrix
