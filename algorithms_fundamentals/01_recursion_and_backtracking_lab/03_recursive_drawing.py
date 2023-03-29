# https://judge.softuni.org/Contests/Practice/Index/3459#2

def draw_fig(n):
    if n < 1:
        return
    print('*' * n)
    draw_fig(n - 1)
    print('#' * n)


num = int(input())

draw_fig(num)
