# https://judge.softuni.org/Contests/Practice/Index/3623#1

def generate_dp_matrix(seq, group_size):
    dp = seq[:group_size]
    for idx in range(group_size, len(seq)):
        dp += [min(dp[idx - group_size: idx]) + seq[idx]]
    return dp


size = 4
sequence = [int(x) for x in input().split()]
dp_matrix = generate_dp_matrix(sequence, size)

print(min(dp_matrix[-size:]))
