#include <stdio.h>

#define INF 9999
#define MAX 20

struct Edge {
    int u, v, w;
};

int main() {
    struct Edge edge[MAX];
    int dist[MAX];
    int n, e, i, j, src;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter number of edges: ");
    scanf("%d", &e);

    printf("Enter edges (u v w):\n");
    for (i = 0; i < e; i++)
        scanf("%d %d %d", &edge[i].u, &edge[i].v, &edge[i].w);

    printf("Enter source vertex: ");
    scanf("%d", &src);

    // Initialize distances
    for (i = 0; i < n; i++)
        dist[i] = INF;
    dist[src] = 0;

    // Relax edges n-1 times
    for (i = 1; i < n; i++) {
        for (j = 0; j < e; j++) {
            int u = edge[j].u;
            int v = edge[j].v;
            int w = edge[j].w;
            if (dist[u] != INF && dist[u] + w < dist[v])
                dist[v] = dist[u] + w;
        }
    }

    // Check for negative weight cycles
    for (j = 0; j < e; j++) {
        int u = edge[j].u;
        int v = edge[j].v;
        int w = edge[j].w;
        if (dist[u] != INF && dist[u] + w < dist[v]) {
            printf("\nGraph contains a negative weight cycle!\n");
            return 0;
        }
    }

    printf("\nShortest distances from vertex %d:\n", src);
    for (i = 0; i < n; i++)
        printf("To %d = %d\n", i, dist[i]);

    return 0;
}
