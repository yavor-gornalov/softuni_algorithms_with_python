# https://judge.softuni.org/Contests/Practice/Index/3474#1
from collections import deque


def construct_dp_matrix(first, second):
    """
    :param first: First sequence of elements
    :param second: Second sequence of elements
    :return: DP matrix
    """
    rows = len(first) + 1
    cols = len(second) + 1
    dp = [[0] * cols for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            if first[row - 1] == second[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    return dp


def reconstruct_path(first, second, dp):
    """
    :param first: First sequence of elements
    :param second: Second sequence of elements
    :param: DP matrix
    :return: Reconstructed Path
    """
    path = deque()
    row = len(dp) - 1
    col = len(dp[0]) - 1

    while row >= 0 and col >= 0:
        if first[row - 1] == second[col - 1]:
            path.appendleft(first[row - 1])
            row -= 1
            col -= 1
        elif dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return path


first_seq = input().split()
second_seq = input().split()

# Problem type: Longest Common Subsequence
dp_matrix = construct_dp_matrix(first_seq, second_seq)
longest_subsequence = reconstruct_path(first_seq, second_seq, dp_matrix)

print(f"{' '.join(x for x in longest_subsequence)}\n"
      f"{len(longest_subsequence)}")
