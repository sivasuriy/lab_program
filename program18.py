INF = 9999999

def prims(graph, V):
    selected = [False] * V
    no_edge = 0
    selected[0] = True

    print("\nEdge : Weight")
    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        no_edge += 1


# -------- MAIN PROGRAM --------
V = int(input("Enter number of vertices: "))
graph = []

print("\nEnter adjacency matrix (use 0 where no edge exists):")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

prims(graph, V)
