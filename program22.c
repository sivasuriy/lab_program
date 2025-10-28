#include <stdio.h>
#define INF 999999
#define MAX 20

int main() {
    int n, i, j, k, L, q;
    int p[MAX], m[MAX][MAX];

    printf("Enter number of matrices: ");
    scanf("%d", &n);

    printf("Enter dimensions (size n+1): ");
    for (i = 0; i <= n; i++)
        scanf("%d", &p[i]);

    // Initialize diagonal to 0
    for (i = 1; i <= n; i++)
        m[i][i] = 0;

    // L is chain length
    for (L = 2; L <= n; L++) {
        for (i = 1; i <= n - L + 1; i++) {
            j = i + L - 1;
            m[i][j] = INF;
            for (k = i; k < j; k++) {
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (q < m[i][j])
                    m[i][j] = q;
            }
        }
    }

    printf("\nMinimum number of multiplications: %d\n", m[1][n]);
    return 0;
}
