# https://judge.softuni.org/Contests/Practice/Index/4041#2

from collections import deque


def create_dp_matrix(matrix):
    # create dp matrix
    dp_matrix = [[0] * size for _ in range(size)]
    dp_matrix[0][0] = matrix[0][0]

    for idx in range(1, size):
        dp_matrix[idx][0] = dp_matrix[idx - 1][0] + matrix[idx][0]
        dp_matrix[0][idx] = dp_matrix[0][idx - 1] + matrix[0][idx]

    for r in range(1, size):
        for c in range(1, size):
            dp_matrix[r][c] = max(dp_matrix[r - 1][c], dp_matrix[r][c - 1]) + matrix[r][c]

    return dp_matrix


def reconstruct_path(dp_matrix):
    row = col = len(dp_matrix) - 1
    path = deque()

    while row > 0 and col > 0:
        path.appendleft((row, col))
        if dp_matrix[row - 1][col] > dp_matrix[row][col - 1]:
            row -= 1
        else:
            col -= 1
    for i in range(row, 0, -1):
        path.appendleft((i, 0))
    for j in range(col, 0, -1):
        path.appendleft((0, j))
    path.appendleft((0, 0))

    return path


size = int(input())

grid = [[int(x) for x in input().split()] for _ in range(size)]

# set abandoned cells to -inf
for cell in input().split():
    r, c = [int(x) for x in cell.split(",")]
    grid[r][c] = float("-inf")

dp = create_dp_matrix(grid)

result = reconstruct_path(dp)

print(f"Max total fertility: {dp[size - 1][size - 1]}")
print(f"[{' '.join([str(s) for s in result])}]")
