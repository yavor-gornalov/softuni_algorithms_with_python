# https://judge.softuni.org/Contests/Practice/Index/3460#1

def print_nested_loops_recursion(idx, vect):
    if idx >= len(vect):
        print(*vect, sep=' ')
        return
    for num in range(1, len(vect) + 1):
        vect[idx] = num
        print_nested_loops_recursion(idx + 1, vect)


n = int(input())
arr = [None] * n

print_nested_loops_recursion(idx=0, vect=arr)
