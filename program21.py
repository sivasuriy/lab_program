# Dynamic Programming - Top Down (Memoization) and Bottom Up (Tabulation)

# ---- TOP-DOWN (Memoization) ----
def fibonacci_top_down(n, memo):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]

    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)
    return memo[n]


# ---- BOTTOM-UP (Tabulation) ----
def fibonacci_bottom_up(n):
    if n <= 1:
        return n

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# ---- MAIN PROGRAM ----
n = int(input("Enter n (for Fibonacci): "))

# Top-Down
memo = [-1] * (n + 1)
print("\nTop-Down DP (Memoization):", fibonacci_top_down(n, memo))

# Bottom-Up
print("Bottom-Up DP (Tabulation):", fibonacci_bottom_up(n))
