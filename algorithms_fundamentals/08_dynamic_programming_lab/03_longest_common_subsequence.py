# https://judge.softuni.org/Contests/Practice/Index/3471#2

from collections import deque

first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = [[0] * cols for _ in range(rows)]

# Calculating the Longest Common Subsequence (LCS) - Table
for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

# Reconstructing the LCS Sequence
row = rows - 1
col = cols - 1
path = deque()
while row >= 0 and col >= 0:
    if first[row - 1] == second[col - 1]:
        path.appendleft(first[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1
# print(", ".join(path))

print(dp[rows - 1][cols - 1])
