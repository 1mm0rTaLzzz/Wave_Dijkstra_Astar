import pandas as pd
import numpy as np


def euclidean_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.linalg.norm(point2 - point1)
    return distance


def solve(matrix, start, end):
    wavefront = np.array([[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))], dtype=np.float64)
    wavefront[start[0]][start[1]] = 1
    wave_value = 1

    while wavefront[end[0]][end[1]] == -1:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if wavefront[i][j] >= wave_value:
                    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1),
                                 (i - 1, j + 1), (i + 1, j - 1)]
                    for neighbor in neighbors:
                        if neighbor[0] >= 0 and neighbor[0] < len(matrix) and neighbor[1] >= 0 and neighbor[1] < len(
                                matrix[0]):
                            if neighbor == (i - 1, j - 1) or neighbor == (i + 1, j + 1) or neighbor == (
                                    i - 1, j + 1) or neighbor == (i + 1, j - 1):
                                if (wavefront[neighbor[0]][neighbor[1]] > wavefront[i][j] + np.sqrt(2) or
                                    wavefront[neighbor[0]][neighbor[1]] == -1) and matrix[neighbor[0]][
                                    neighbor[1]] == 0:
                                    wavefront[neighbor[0]][neighbor[1]] = wavefront[i][j] + np.sqrt(2)
                            else:
                                if (wavefront[neighbor[0]][neighbor[1]] > wavefront[i][j] + 1 or wavefront[neighbor[0]][
                                    neighbor[1]] == -1) and matrix[neighbor[0]][neighbor[1]] == 0:
                                    wavefront[neighbor[0]][neighbor[1]] = wavefront[i][j] + 1
        wave_value += 1
    df = pd.DataFrame(wavefront)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(df)
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if wavefront[i][j] != -1:
                wavefront[i][j] += euclidean_distance((i, j), end)


    matrix = wavefront
    print(df)
    # print(min)

    way = np.array([[], []], dtype=np.int16)
    move = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]])  # 8 move ver
    # move = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]]) # 4 move ver
    print('Point start', end, '\n', 'Point end', start)
    '''
    temp_x, temp_y = end[0], end[1]
    min_ = 100
    count = 0
    while temp_x != start[0] or temp_y != start[1] and count < 100:
        count += 1
        check = True
        for m in move:
            if matrix[temp_x + m[0]][temp_y + m[1]] != -1 and check:
                min_ = matrix[temp_x + m[0]][temp_y + m[1]]
                check = False
            print(min_)
            step_x = temp_x + m[0]
            step_y = temp_y + m[1]
            try:
                if min_ >= matrix[step_x][step_y] and matrix[step_x][step_y] != -1 and step_x >= 0 and step_y >= 0:
                    min_ = matrix[step_x][step_y]
                    min_x, min_y = step_x, step_y

            except Exception:
                pass

        temp_x, temp_y = min_x, min_y
        way = np.append(way, np.array([temp_x, temp_y]))
    '''
    way = way.reshape(-1, 2)
    print(way)
    return way, matrix

