# https://judge.softuni.org/Contests/Compete/Index/3473#1

first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = [[0] * cols for _ in range(rows)]

for i in range(1, rows):
    dp[i][0] = i

for j in range(1, cols):
    dp[0][j] = j

for r in range(1, rows):
    for c in range(1, cols):
        if first[r - 1] == second[c - 1]:
            dp[r][c] = dp[r - 1][c - 1]
        else:
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + 1

print(f"Deletions and Insertions: {dp[rows - 1][cols - 1]}")
