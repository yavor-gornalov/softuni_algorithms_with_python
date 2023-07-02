# https://judge.softuni.org/Contests/Practice/Index/3471#0

def fibonacci_recursive(n, memo):
    if n < 2:
        memo[n] = n
        return n

    if n in memo:
        return memo[n]

    result = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    memo[n] = result
    return result


number = int(input())
print(fibonacci_recursive(number, {}))
