# Python program to implement A* search algorithm
from heapq import heappush, heappop

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f_cost, g_cost, node, path)
    open_list = []
    heappush(open_list, (heuristic[start], 0, start, [start]))

    visited = {}

    while open_list:
        f_cost, g_cost, current, path = heappop(open_list)

        if current == goal:
            return path, g_cost

        if current in visited and visited[current] <= g_cost:
            continue

        visited[current] = g_cost

        for neighbor, cost in graph[current]:
            new_g = g_cost + cost
            new_f = new_g + heuristic[neighbor]
            heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')


# Graph represented as adjacency list
graph = {
    'A': [('B', 0), ('C', 4)],
    'B': [('D', 3), ('E', 2)],
    'C': [('F', 7)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values (estimated cost to goal G)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")