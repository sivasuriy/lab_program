import sys

def dijkstra(graph, start):
    V = len(graph)
    distance = [sys.maxsize] * V
    visited = [False] * V

    distance[start] = 0

    for _ in range(V):
        # Find vertex with minimum distance
        min_dist = sys.maxsize
        min_index = -1

        for v in range(V):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                min_index = v

        visited[min_index] = True

        # Update distance values
        for v in range(V):
            if graph[min_index][v] != 0 and not visited[v]:
                new_dist = distance[min_index] + graph[min_index][v]
                if new_dist < distance[v]:
                    distance[v] = new_dist

    return distance


# -------- MAIN PROGRAM --------
V = int(input("Enter number of vertices: "))
graph = []

print("\nEnter adjacency matrix (use 0 where no edge exists):")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting vertex (0 to V-1): "))
result = dijkstra(graph, start)

print("\nShortest distances from vertex", start)
for i in range(V):
    print(f"{start} → {i} = {result[i]}")
