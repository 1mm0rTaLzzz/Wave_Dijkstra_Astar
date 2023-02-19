import numpy as np
import sys


def create_adjacency_matrix(matrix):
    n = len(matrix)
    adjacency_matrix = np.array([[0] * n for _ in range(n)])
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -1:
                adjacency_matrix[i][j] = 1
    return adjacency_matrix


def minDistance(distances, visited):
    min_distance = sys.maxsize
    min_index = 0
    for v in range(len(distances)):
        if distances[v] < min_distance and not visited[v]:
            min_distance = distances[v]
            min_index = v
    return min_index


def printSolution(distances):
    print("Vertex \t Distance from Source")
    for i in range(len(distances)):
        print(i, "\t", distances[i])


def dijkstra(graph, source):
    num_vertices = len(graph)

    distances = [sys.maxsize] * num_vertices
    distances[source] = 0

    visited = [False] * num_vertices
    for i in range(num_vertices):

        u = minDistance(distances, visited)

        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]

    printSolution(distances)


if __name__ == '__main__':
    win_size = (600, 600)
    cell_size = 50
    rows = win_size[1] // cell_size
    cols = win_size[0] // cell_size

    matrix = np.array([[0 for j in range(cols)] for i in range(rows)])
    matrix[1][3] = -1
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    dijkstra(graph, 1)
    print(matrix)
    print(create_adjacency_matrix(matrix))
