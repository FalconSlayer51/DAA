def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D dp array, where dp[i][j] represents the maximum value for capacity j using first i items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # The result will be in dp[n][capacity]
    return dp[n][capacity]

# Example usage
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
print(knapsack(weights, values, capacity))  # Output: 9
