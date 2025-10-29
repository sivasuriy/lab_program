import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def addEdge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        distances = {node: float('inf') for node in self.graph}
        distances[src] = 0

        pq = [(0, src)]  # priority queue: (distance, node)

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        print("\nShortest distances from source:", src)
        for node in distances:
            print(f"{src} -> {node} = {distances[node]}")


# ---------- MAIN PROGRAM ----------
vertices = int(input("Enter number of vertices: "))
g = Graph(vertices)

while True:
    print("\n--- Dijkstra's Algorithm Menu ---")
    print("1. Add weighted edge")
    print("2. Find shortest path")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        u = input("Enter starting vertex: ")
        v = input("Enter ending vertex: ")
        w = int(input("Enter weight: "))
        g.addEdge(u, v, w)
        print("Edge added successfully!")

    elif ch == 2:
        src = input("Enter source vertex: ")
        g.dijkstra(src)

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
