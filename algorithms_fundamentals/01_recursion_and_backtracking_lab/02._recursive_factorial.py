# https://judge.softuni.org/Contests/Practice/Index/3459#1

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


n = int(input())

print(factorial(n))
