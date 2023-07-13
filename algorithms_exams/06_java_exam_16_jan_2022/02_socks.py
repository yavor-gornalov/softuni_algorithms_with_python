# https://judge.softuni.org/Contests/Practice/Index/3347#1

def longest_common_sequence_count(first_seq, second_seq):
    rows = len(first_seq) + 1
    cols = len(second_seq) + 1

    dp = []
    [dp.append([0] * cols) for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            if first_seq[row - 1] == second_seq[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    return dp[rows - 1][cols - 1]


left_socks = input().split()
right_socks = input().split()

count = longest_common_sequence_count(left_socks, right_socks)

print(count)
