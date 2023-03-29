# https://judge.softuni.org/Contests/Practice/Index/3459#6

def recursive_fibonacci(num):
    if num <= 1:
        return 1
    return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)


def iterative_fibonacci(num):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(num - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


number = int(input())
print(iterative_fibonacci(number))
