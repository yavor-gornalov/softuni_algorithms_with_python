# https://judge.softuni.org/Contests/Practice/Index/2484#1

from sys import maxsize

costs = [int(x) for x in input().split()]
flasks_count = int(input())

size = flasks_count + 1
dp = [0] * size
prev = [-1] * size

for i in range(1, size):
    dp[i] = maxsize
    for j in range(1, i + 1):
        if j > len(costs):
            break
        current_cost = dp[i - j] + costs[j - 1]
        if current_cost < dp[i]:
            dp[i] = current_cost
            prev[i] = j

print(f"Cost: {dp[size - 1]}")

path = []
p = flasks_count
while p > 0:
    path.append(f"{prev[p]} => {costs[prev[p] - 1]}" )
    p -= prev[p]

print(*path, sep="\n")
