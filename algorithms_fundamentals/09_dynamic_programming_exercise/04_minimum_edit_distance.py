# https://judge.softuni.org/Contests/Compete/Index/3473#3

replacement_cost = int(input())
insert_cost = int(input())
delete_cost = int(input())

first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1
dp = [[0] * cols for _ in range(rows)]

for r in range(1, rows):
    dp[r][0] = dp[r - 1][0] + delete_cost

for c in range(1, cols):
    dp[0][c] = dp[0][c - 1] + insert_cost

for r in range(1, rows):
    for c in range(1, cols):
        if first[r - 1] == second[c - 1]:
            dp[r][c] = dp[r - 1][c - 1]
        else:
            dp[r][c] = min(
                dp[r - 1][c] + delete_cost,
                dp[r][c - 1] + insert_cost,
                dp[r - 1][c - 1] + replacement_cost
            )

print(f"Minimum edit distance: {dp[rows - 1][cols - 1]}")
