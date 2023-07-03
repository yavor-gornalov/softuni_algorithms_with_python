# https://judge.softuni.org/Contests/Compete/Index/3471#3

from collections import deque

nums = [int(x) for x in input().split()]

# Calculating Longest Increasing Subsequence (LIS) with Previous
size = [0] * len(nums)
parent = [None] * len(nums)
best_len, best_idx = 0, 0
for curr_idx in range(len(nums)):
    curr_num = nums[curr_idx]
    curr_len = 1
    curr_parent = None
    for prev_idx in range(curr_idx - 1, -1, -1):
        prev_number = nums[prev_idx]
        prev_len = size[prev_idx]

        if prev_number >= curr_num:
            continue

        if prev_len + 1 >= curr_len:
            curr_len = prev_len + 1
            curr_parent = prev_idx

    size[curr_idx] = curr_len
    parent[curr_idx] = curr_parent
    if curr_len > best_len:
        best_len = curr_len
        best_idx = curr_idx

# Restoring LIS Elements
result = deque()
idx = best_idx
while idx is not None:
    result.appendleft(nums[idx])
    idx = parent[idx]
print(*result, sep=' ')
