# https://judge.softuni.org/Contests/Practice/Index/4004#2

"""
This is a problem from Algorithms with Java course.
Python to Java converter used for testing the code in judge system
"""

from collections import deque


def get_lcs_matrix(first_seq, second_seq):
    rows = len(first_seq) + 1
    cols = len(second_seq) + 1
    dp = [[0] * cols for _ in range(rows)]

    # Calculating the Longest Common Subsequence (LCS) - Table
    for row in range(1, rows):
        for col in range(1, cols):
            if first_seq[row - 1] == second_seq[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    return dp


def reconstruct_lcs_sequence(first_seq, second_seq, dp):
    # Reconstructing the LCS Sequence
    row = len(first_seq)
    col = len(second_seq)
    path = deque()
    while row > 0 and col > 0:
        if first_seq[row - 1] == second_seq[col - 1]:
            path.appendleft(first_seq[row - 1])
            row -= 1
            col -= 1
        elif dp[row - 1][col] >= dp[row][col - 1]:
            row -= 1
        else:
            col -= 1
    return path


first = input().split()
second = input().split()

lcs_matrix = get_lcs_matrix(first, second)

result = reconstruct_lcs_sequence(first, second, lcs_matrix)

print(f"[{' '.join(result)}]")
