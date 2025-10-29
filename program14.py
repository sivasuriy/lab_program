from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, start):
        visited = set()
        print("DFS Traversal starting from node", start, ": ", end="")
        self.DFSUtil(start, visited)
        print()


# -------- MAIN PROGRAM --------
g = Graph()

while True:
    print("\n--- DFS GRAPH MENU ---")
    print("1. Add Edge")
    print("2. Perform DFS Traversal")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        u = input("Enter starting vertex: ")
        v = input("Enter ending vertex: ")
        g.addEdge(u, v)
        print("Edge added successfully!")

    elif ch == 2:
        start = input("Enter starting vertex for DFS: ")
        g.DFS(start)

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
