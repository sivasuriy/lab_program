#include <stdio.h>

#define INF 9999
#define MAX 20

int main() {
    int n, i, j, u, v, ne = 1;
    int visited[MAX] = {0};
    int min, mincost = 0;
    int cost[MAX][MAX];

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix (0 for no edge):\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
            if (cost[i][j] == 0)
                cost[i][j] = INF;
        }

    visited[0] = 1; // start from vertex 0

    printf("\nEdges in Minimum Spanning Tree:\n");
    while (ne < n) {
        min = INF;
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
                if (cost[i][j] < min && visited[i] && !visited[j]) {
                    min = cost[i][j];
                    u = i;
                    v = j;
                }

        printf("%d -> %d = %d\n", u, v, min);
        mincost += min;
        visited[v] = 1;
        ne++;
        cost[u][v] = cost[v][u] = INF;
    }

    printf("\nMinimum Cost = %d\n", mincost);

    return 0;
}
