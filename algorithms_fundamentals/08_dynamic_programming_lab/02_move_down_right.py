# https://judge.softuni.org/Contests/Practice/Index/3471#1
from collections import deque

rows = int(input())
cols = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

dp = [[0] * cols for _ in range(rows)]
# First, find all base solutions
dp[0][0] = matrix[0][0]
for r in range(cols):
    dp[r][0] = dp[r - 1][0] + matrix[r][0]
for c in range(cols):
    dp[0][c] = dp[0][c - 1] + matrix[0][c]
# Fill rest of the cells
for r in range(1, rows):
    for c in range(1, cols):
        dp[r][c] = matrix[r][c] + max(dp[r - 1][c], dp[r][c - 1])

r = rows - 1
c = cols - 1
path = deque()
while r > 0 and c > 0:
    path.appendleft([r, c])
    if dp[r - 1][c] > dp[r][c - 1]:
        r -= 1
    else:
        c -= 1
for i in range(r, 0, -1):
    path.appendleft([i, 0])
for j in range(c, 0, -1):
    path.appendleft([0, j])
path.appendleft([0, 0])

print(*path, sep=" ")
