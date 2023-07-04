# https://judge.softuni.org/Contests/Compete/Index/3473#4

from collections import deque

strings = input().split()

# Calculating Longest Increasing Subsequence (LIS) with Previous
size = [0] * len(strings)
parent = [None] * len(strings)
best_sequence_len, best_idx = 0, 0
for curr_idx in range(len(strings)):
    curr_str_len = len(strings[curr_idx])
    curr_sequence_len = 1
    curr_parent = None
    for prev_idx in range(curr_idx - 1, -1, -1):
        prev_str_len = len(strings[prev_idx])
        prev_sequence_len = size[prev_idx]

        if prev_str_len >= curr_str_len:
            continue

        if prev_sequence_len + 1 >= curr_sequence_len:
            curr_sequence_len = prev_sequence_len + 1
            curr_parent = prev_idx

    size[curr_idx] = curr_sequence_len
    parent[curr_idx] = curr_parent
    if curr_sequence_len > best_sequence_len:
        best_sequence_len = curr_sequence_len
        best_idx = curr_idx

# Restoring LIS Elements
result = deque()
idx = best_idx
while idx is not None:
    result.appendleft(strings[idx])
    idx = parent[idx]
print(*result, sep=' ')
