import heapq

graph = {
    'Home': ['Park', 'Market'],
    'Park': ['School', 'Cafe'],
    'Market': ['School', 'College'],
    'School': [],
    'Cafe': [],
    'Hospital': [],
    'College': []
}

Heuristic = {
    'Home': 10,
    'Park': 7,
    'Market': 4,
    'School': 8,
    'Cafe': 6,
    'Hospital': 3,
    'College': 0
}


def best_first_search(start, goal):

    priority_queue = []
    visited = set()

    heapq.heappush(priority_queue, (Heuristic[start], start))

    print("Initial State:", start)
    print("Goal State:", goal)
    print("\nSearch Path:")

    while priority_queue:

        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        print(f"{current} (h = {h})", end="")

        if current == goal:
            print("\n\nGoal Found!")
            return

        print(" -> ", end="")

        for neighbour in graph[current]:

            if neighbour not in visited:
                print(f"{neighbour}(h={Heuristic[neighbour]}) ", end="")

                heapq.heappush(
                    priority_queue,
                    (Heuristic[neighbour], neighbour)
                )

    print("\nGoal not found")


best_first_search('Home', 'College')