coins = [int(x) for x in input().split()]
target = int(input())

# DP matrix for dynamic programming
dp = [1] + [0] * target

for coin in coins:
    for j in range(coin, target + 1):
        dp[j] += dp[j - coin]

print(dp[target])
