# https://judge.softuni.org/Contests/Compete/Index/3473#2

cables = [int(x) for x in input().split()]

size = len(cables) + 1
sockets = [int(s) for s in range(1, size)]

dp = [[0] * size for _ in range(size)]

for row in range(1, size):
    for col in range(1, size):
        if cables[row - 1] == sockets[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(f"Maximum pairs connected: {dp[size - 1][size - 1]}")
