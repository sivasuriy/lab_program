from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        # Calculate indegree of all vertices
        in_degree = {i: 0 for i in self.graph}

        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] = in_degree.get(v, 0) + 1

        queue = deque([node for node in in_degree if in_degree[node] == 0])
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(topo_order) != len(in_degree):
            print("Graph has a cycle! Topological sort not possible.")
        else:
            print("Topological Sort:", " → ".join(topo_order))


# -------- MAIN PROGRAM --------
vertices = int(input("Enter number of vertices: "))
g = Graph(vertices)

while True:
    print("\n--- Topological Sort Menu ---")
    print("1. Add edge")
    print("2. Perform Topological Sort")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        u = input("Enter starting vertex: ")
        v = input("Enter ending vertex: ")
        g.addEdge(u, v)
        print("Edge added successfully!")

    elif ch == 2:
        g.topologicalSort()

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
