# https://judge.softuni.org/Contests/Practice/Index/3346#2

from collections import deque


def generate_reversed_dp_matrix(matirx):
    rows = len(matirx)
    cols = len(matirx[0])

    dp = [[0] * cols for _ in range(rows)]

    # First, find all base solutions
    dp[rows - 1][cols - 1] = matrix[rows - 1][cols - 1]
    for r in range(rows - 2, -1, -1):
        dp[r][cols - 1] = dp[r + 1][cols - 1] + matrix[r][cols - 1]
    for c in range(cols - 2, -1, -1):
        dp[rows - 1][c] = dp[rows - 1][c + 1] + matrix[rows - 1][c]

    # Fill rest of the cells
    for r in range(rows - 2, -1, -1):
        for c in range(cols - 2, -1, -1):
            dp[r][c] = matrix[r][c] + max(dp[r + 1][c], dp[r][c + 1])

    return dp


def reconstuct_path(dp, matrix):
    rows = len(dp_matrix)
    cols = len(dp_matrix[0])
    path = deque()

    r = c = 0
    while r < rows - 1 and c < cols - 1:
        path.appendleft(matrix[r][c])
        if dp[r + 1][c] > dp[r][c + 1]:
            r += 1
        else:
            c += 1
    for i in range(r, rows - 1):
        path.appendleft(matrix[i][rows - 1])
    for j in range(c, cols - 1):
        path.appendleft(matrix[cols - 1][j])
    path.appendleft(matrix[rows - 1][cols - 1])

    return path


rows = int(input())
cols = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

dp_matrix = generate_reversed_dp_matrix(matrix)
path = reconstuct_path(dp_matrix, matrix)

print(dp_matrix[0][0])
print(*path, sep=" ")
