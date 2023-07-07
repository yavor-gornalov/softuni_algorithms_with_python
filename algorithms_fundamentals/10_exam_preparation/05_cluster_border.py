# https://judge.softuni.org/Contests/Practice/Index/2481#1

"""
This is a problem from Algorithms with Java course.
Python to Java converter used for testing the code in judge system
"""
from collections import deque

single_ship_times = [int(x) for x in input().split()]
pair_ship_times = [int(x) for x in input().split()]

size = len(single_ship_times) + 1

dp = [0] * size
dp[1] = single_ship_times[0]

for idx in range(2, size):
    current_ship_time = dp[idx - 1] + single_ship_times[idx - 1]
    current_pair_time = dp[idx - 2] + pair_ship_times[idx - 2]
    dp[idx] = min(current_ship_time, current_pair_time)

passing_list = deque()
idx = size - 1
while idx:
    if dp[idx] - dp[idx - 1] == single_ship_times[idx - 1]:
        passing_list.appendleft(f"Single {idx}")
        idx -= 1
    else:
        passing_list.appendleft(f"Pair of {idx - 1} and {idx}")
        idx -= 2

passing_list.appendleft(f"Optimal Time: {dp[size - 1]}")
for row in passing_list:
    print(row)
