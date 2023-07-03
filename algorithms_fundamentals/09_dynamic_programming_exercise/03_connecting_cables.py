# https://judge.softuni.org/Contests/Compete/Index/3473#2

nums = [int(x) for x in input().split()]

# Calculating Longest Increasing Subsequence (LIS) with Previous
size = [0] * len(nums)
best_len = 0
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
    best_len = max(curr_len, best_len)

print(f"Maximum pairs connected: {best_len}")
