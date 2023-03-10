import sys
import numpy as np
from math import sqrt


def get_adjacency_matrix(field):
    # Determine the number of nodes and create an empty matrix
    num_nodes = len(field) * len(field[0])
    adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=np.float64)

    # Define the eight-cell neighborhood
    neighborhood = np.array([(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0])

    # Iterate over all nodes and their neighbors to fill in the adjacency matrix
    for i in range(len(field)):
        for j in range(len(field[0])):
            node_index = i * len(field[0]) + j
            if field[i][j] != -1:
                for ni, nj in neighborhood:
                    if (i + ni >= 0 and i + ni < len(field) and j + nj >= 0 and j + nj < len(field[0])
                            and field[i + ni][j + nj] != -1):
                        neighbor_index = (i + ni) * len(field[0]) + (j + nj)
                        if node_index == neighbor_index:
                            adjacency_matrix[node_index][neighbor_index] = sqrt(2)
                        elif abs(ni) + abs(nj) == 2:
                            adjacency_matrix[node_index][neighbor_index] = sqrt(2)
                        else:
                            adjacency_matrix[node_index][neighbor_index] = 1

    return adjacency_matrix.reshape(144, 144)


def minDistance(distances, visited):
    min_distance = sys.maxsize
    min_index = 0
    for v in range(len(distances)):
        if distances[v] < min_distance and not visited[v]:
            min_distance = distances[v]
            min_index = v
        '''
        for i in distances:
            print(i)
        '''
    return min_index


def dijkstra(graph, source, destination):
    num_vertices = len(graph)

    distances = [sys.maxsize] * num_vertices
    distances[source] = 0

    parent = [-1] * num_vertices
    visited = [False] * num_vertices

    for i in range(num_vertices - 1):
        u = minDistance(distances, visited)
        visited[u] = True
        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
                parent[v] = u

    path = []
    current = destination
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return path
