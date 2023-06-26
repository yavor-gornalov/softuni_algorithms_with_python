# https://judge.softuni.org/Contests/Practice/Index/3623#1
# from sys import maxsize
# from collections import deque
#
#
# def find_minimum_sum(seq):
#     total_sum = 0
#     step = 4
#     while seq:
#         min_num = maxsize
#         count = min(len(seq), step)
#         for _ in range(count):
#             min_num = min(min_num, seq.popleft())
#         total_sum += min_num
#     return total_sum
#
#
# sequence = deque(int(x) for x in input().split())
#
# print(find_minimum_sum(sequence))


def find_min_sum_subsequence(row, col, matrix):
    if row < 0 or col < 0 or row > len(matrix) or col > len(matrix[0]):
        return
    if matrix[row][col] == float("inf"):
        return
    if row == len(matrix):
        return matrix[row][col]

    result = 0
    result += find_min_sum_subsequence(row + 1, col, matrix)
    result += find_min_sum_subsequence(row, col + 1, matrix)

    return result


# sequence = [int(x) for x in input().split()]
sequence = [11, 34, 23, 8, 1, 3, 5, 13, 4, 69]

dp = []
[dp.append([]) for _ in range(len(sequence) - 3)]

for idx in range(len(sequence) - 3):
    dp[idx] = [float("inf")] * idx + sequence[idx:idx + 4] + [float("inf")] * (len(sequence) - 4 - idx)
    print(*dp[idx], sep=" ")

min_sum = find_min_sum_subsequence(0, 0, dp)
print(min_sum)
