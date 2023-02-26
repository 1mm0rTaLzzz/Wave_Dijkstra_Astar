
import math
import heapq


def astar(start, end, matrix):
    # Define helper functions
    def heuristic(a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def neighbors(point):
        row, col = point
        # Define possible neighbors
        possible_neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                              (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
        # Filter out neighbors that are walls or out of bounds
        valid_neighbors = []
        for neighbor in possible_neighbors:
            row, col = neighbor
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] != -1:
                # Set cost to sqrt(2) for diagonal movements, and 1 for up/down/left/right movements
                if neighbor[0] == point[0] or neighbor[1] == point[1]:
                    valid_neighbors.append((neighbor, 1))
                else:
                    valid_neighbors.append((neighbor, math.sqrt(2)))
        return valid_neighbors

    # Define priority queue and starting values
    queue = []
    visited = set()
    heapq.heappush(queue, (0, start, [start]))

    # Loop until queue is empty
    while queue:
        # Pop the lowest priority node from the queue
        cost, current, path = heapq.heappop(queue)

        # Check if we have reached the end
        if current == end:
            return path

        # Check if we have already visited this node
        if current in visited:
            continue

        # Add current node to visited set
        visited.add(current)

        # Get the neighbors of the current node
        for neighbor, neighbor_cost in neighbors(current):
            # Calculate the cost to reach the neighbor node
            neighbor_cost = cost + neighbor_cost

            # Calculate the heuristic cost of the neighbor node
            neighbor_heuristic = heuristic(neighbor, end)

            # Add the neighbor node to the queue with the total cost
            heapq.heappush(queue, (neighbor_cost + neighbor_heuristic, neighbor, path + [neighbor]))

    # If we reach here, there is no path from start to end
    return None
