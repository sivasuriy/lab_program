#include <stdio.h>

#define INF 9999
#define MAX 20

void dijkstra(int graph[MAX][MAX], int n, int start) {
    int cost[MAX][MAX], distance[MAX], visited[MAX], count, minDistance, nextNode, i, j;

    // Create cost matrix
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            cost[i][j] = (graph[i][j] == 0) ? INF : graph[i][j];

    for (i = 0; i < n; i++) {
        distance[i] = cost[start][i];
        visited[i] = 0;
    }

    distance[start] = 0;
    visited[start] = 1;
    count = 1;

    while (count < n - 1) {
        minDistance = INF;

        for (i = 0; i < n; i++)
            if (distance[i] < minDistance && !visited[i]) {
                minDistance = distance[i];
                nextNode = i;
            }

        visited[nextNode] = 1;

        for (i = 0; i < n; i++)
            if (!visited[i])
                if (minDistance + cost[nextNode][i] < distance[i])
                    distance[i] = minDistance + cost[nextNode][i];

        count++;
    }

    printf("\nShortest distances from node %d:\n", start);
    for (i = 0; i < n; i++)
        if (i != start)
            printf("To %d = %d\n", i, distance[i]);
}

int main() {
    int graph[MAX][MAX], n, i, j, start;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter the adjacency matrix (0 for no edge):\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &graph[i][j]);

    printf("Enter the starting node: ");
    scanf("%d", &start);

    dijkstra(graph, n, start);

    return 0;
}
