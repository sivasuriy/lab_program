#include <stdio.h>

#define MAX 50

int memo[MAX];

// ---------- TOP-DOWN (Memoization) ----------
int fibTopDown(int n) {
    if (n <= 1)
        return n;
    if (memo[n] != -1)
        return memo[n];
    memo[n] = fibTopDown(n - 1) + fibTopDown(n - 2);
    return memo[n];
}

// ---------- BOTTOM-UP (Tabulation) ----------
int fibBottomUp(int n) {
    int dp[MAX];
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++)
        dp[i] = dp[i - 1] + dp[i - 2];

    return dp[n];
}

int main() {
    int n, i;
    printf("Enter n (Fibonacci term): ");
    scanf("%d", &n);

    // Initialize memo array with -1
    for (i = 0; i < MAX; i++)
        memo[i] = -1;

    printf("\n--- Top-Down (Memoization) ---\n");
    printf("Fib(%d) = %d\n", n, fibTopDown(n));

    printf("\n--- Bottom-Up (Tabulation) ---\n");
    printf("Fib(%d) = %d\n", n, fibBottomUp(n));

    return 0;
}
