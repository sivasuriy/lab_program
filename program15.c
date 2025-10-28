#include <stdio.h>

#define MAX 20

int adj[MAX][MAX];
int visited[MAX];
int stack[MAX];
int top = -1;
int n;

void push(int v) {
    stack[++top] = v;
}

int pop() {
    return stack[top--];
}

void topoSortDFS(int v) {
    visited[v] = 1;
    for (int i = 0; i < n; i++) {
        if (adj[v][i] == 1 && !visited[i])
            topoSortDFS(i);
    }
    push(v);
}

int main() {
    int i, j;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &adj[i][j]);

    for (i = 0; i < n; i++)
        visited[i] = 0;

    for (i = 0; i < n; i++)
        if (!visited[i])
            topoSortDFS(i);

    printf("Topological Sort Order: ");
    while (top != -1)
        printf("%d ", pop());
    printf("\n");

    return 0;
}
