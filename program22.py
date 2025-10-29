# Matrix Chain Multiplication using Dynamic Programming

import sys

def matrix_chain_order(p):
    n = len(p) - 1

    # Table to store minimum number of multiplications
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # L = chain length
    for L in range(2, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1
            dp[i][j] = sys.maxsize   # Initialize with big value

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


# ---- MAIN PROGRAM ----
print("Matrix Chain Multiplication using Dynamic Programming\n")

n = int(input("Enter number of matrices: "))
arr = []

print("Enter dimensions (Example for 3 matrices A: 10x20, B: 20x5, C: 5x30")
print("Enter values like: 10 20 5 30\n")

arr = list(map(int, input("Enter dimensions: ").split()))

if len(arr) != n + 1:
    print("Error: For", n, "matrices, enter", n + 1, "dimensions.")
else:
    result = matrix_chain_order(arr)
    print("\nMinimum number of multiplications =", result)
