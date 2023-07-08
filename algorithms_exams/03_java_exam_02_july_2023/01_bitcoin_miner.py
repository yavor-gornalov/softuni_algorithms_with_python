# https://judge.softuni.org/Contests/Practice/Index/4004#0

def calc_binomial_coefficient(n, k, memo):
    if n <= 1 or k < 1 or k >= n:
        return 1

    if (n, k) in memo:
        return memo[(n, k)]

    result = calc_binomial_coefficient(n - 1, k, memo) + calc_binomial_coefficient(n - 1, k - 1, memo)
    memo[(n, k)] = result
    return result


transactions_count = int(input())
transactions_could_be_picked = int(input())
print(calc_binomial_coefficient(transactions_count, transactions_could_be_picked, {}))
