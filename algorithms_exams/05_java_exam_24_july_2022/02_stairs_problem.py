# # https://judge.softuni.org/Contests/Practice/Index/3563#1

# def stairs_combinations_recursive(idx, vect):
#     if idx == len(vect):
#         return 1
#
#     combinations = 0
#     low_limit = 0
#     if idx > 0:
#         if vect[idx - 1] == 0:
#             low_limit = 1
#
#     for num in range(low_limit, 2):
#         vect[idx] = num
#         combinations += stairs_combinations_recursive(idx + 1, vect)
#
#     return combinations


def stairs_combinations(stairs):
    if stairs == 0:
        return 1

    dp = [0] * (stairs + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, stairs + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[stairs]


stairs = int(input())
result = stairs_combinations(stairs)
print(result)
