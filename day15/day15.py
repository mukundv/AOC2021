import heapq
from collections import defaultdict
from math import inf

from utils import timeit, generate_readme


def get_input(input_file_name):
    with open(input_file_name) as f:
        return list(list(map(int, row)) for row in map(str.rstrip, f))


def get_neighbours(row, col, height, width):
    for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        i, j = (row + x, col + y)
        if 0 <= i < width and 0 <= j < height:
            yield i, j


@timeit
def dijkstra(matrix):
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    destination, height, minimum_distance, queue, visited, width = setup_dijkstra(matrix)
    while queue:
        # Get the node with the lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)  # removes and returns the smallest element from the heap

        # If we got to the destination, we have our answer.
        if node == destination:
            return dist

        # If we already visited this node, skip it, proceed to the next one.
        if node in visited:
            continue

        # Mark the node as visited.
        visited.add(node)
        row, col = node

        # For each unvisited neighbor of this node...
        get_cheaper_path(col, dist, height, matrix, minimum_distance, queue, row, visited, width)
    # If we ever empty the queue without entering the node == destination check
    # in the above loop, there is no path from source to destination!
    return inf


def setup_dijkstra(matrix):
    height, width = len(matrix), len(matrix[0])
    source = (0, 0)  # Top left
    destination = (height - 1, width - 1)  # Bottom right
    minimum_distance = defaultdict(lambda: inf, {source: 0})  # Initialise with infinity
    queue = [(0, source)]
    visited = set()
    return destination, height, minimum_distance, queue, visited, width


def get_cheaper_path(col, dist, height, matrix, minimum_distance, queue, row, visited, width):
    for neighbor in get_neighbours(row, col, height, width):
        if neighbor in visited:
            continue
        neighbour_row, neighbour_col = neighbor
        new_distance = dist + matrix[neighbour_row][neighbour_col]
        # If the new distance is lower than the minimum distance we have to
        # reach this neighbor, then update its minimum distance and add it
        # to the queue, as we found a "better" path to it.
        if new_distance < minimum_distance[neighbor]:
            minimum_distance[neighbor] = new_distance
            heapq.heappush(queue, (new_distance, neighbor))
            # pushes an element into an existing heap in such a way that the heap property is maintained


def get_bigger_matrix(matrix):
    height, width = len(matrix), len(matrix[0])
    for _ in range(4):
        for row in matrix:
            tail = row[-width:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)
    for _ in range(4):
        for row in matrix[-height:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            matrix.append(row)
    return matrix


if __name__ == '__main__':
    print(f'Part 1: {dijkstra(get_input("day15_input.txt"))}')
    print(f'Part 2: {dijkstra(get_bigger_matrix(get_input("day15_input.txt")))}')
    generate_readme("README", '2021', '15', '../')
