INF = 9999999  # a very large number to represent infinity

def floydWarshall(graph, V):
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    # Floyd Warshall core logic
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[j][k]

    print("\nAll Pair Shortest Path Matrix:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()


# --------- MAIN PROGRAM ---------
V = int(input("Enter number of vertices: "))
graph = []

print("\nEnter adjacency matrix (use 9999999 for INF):")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

floydWarshall(graph, V)
