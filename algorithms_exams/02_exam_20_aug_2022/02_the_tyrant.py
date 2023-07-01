# https://judge.softuni.org/Contests/Practice/Index/3623#1
# modified solution from www.geeksforgeeks.org
def min_sum(seq):
    size = len(seq)
    dp = [0] * size

    if size < 5:
        return min(seq)

    dp[0:4] = seq[0:4]

    for i in range(4, size):
        dp[i] = seq[i] + min(dp[i - 4: i])

    return min(dp[size - 4:size])


sequence = [int(x) for x in input().split()]
print(min_sum(sequence))
