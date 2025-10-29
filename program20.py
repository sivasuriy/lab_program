import sys

def floyd_warshall(graph, V):
    dist = list(map(lambda i: list(i), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# -------- MAIN PROGRAM --------
V = int(input("Enter number of vertices: "))

print("\nEnter adjacency matrix:")
print(" (Use 99999 for INF and 0 for diagonal values)")

graph = []
for _ in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

result = floyd_warshall(graph, V)

print("\nAll-Pairs Shortest Distances Matrix:")
for row in result:
    print(row)
