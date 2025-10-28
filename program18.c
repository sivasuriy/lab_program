#include <stdio.h>

#define MAX 30

int parent[MAX];

// Find parent (used for union-find)
int find(int i) {
    while (parent[i])
        i = parent[i];
    return i;
}

// Union two subsets
int unionSet(int i, int j) {
    if (i != j) {
        parent[j] = i;
        return 1;
    }
    return 0;
}

int main() {
    int cost[MAX][MAX];
    int n, i, j, a, b, u, v, ne = 1;
    int min, mincost = 0;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix (0 for no edge):\n");
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++) {
            scanf("%d", &cost[i][j]);
            if (cost[i][j] == 0)
                cost[i][j] = 9999; // infinity
        }

    printf("\nEdges in Minimum Spanning Tree:\n");
    while (ne < n) {
        min = 9999;

        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                if (cost[i][j] < min) {
                    min = cost[i][j];
                    a = u = i;
                    b = v = j;
                }

        u = find(u);
        v = find(v);

        if (unionSet(u, v)) {
            printf("%d -> %d = %d\n", a, b, min);
            mincost += min;
            ne++;
        }

        cost[a][b] = cost[b][a] = 9999;
    }

    printf("\nMinimum Cost = %d\n", mincost);
    return 0;
}
