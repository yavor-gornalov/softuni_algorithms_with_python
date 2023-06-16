# https://judge.softuni.org/Contests/Practice/Index/3460#1

def nested_loops(vect, idx, size):
    if idx == size:
        print(*vect, sep=" ")
        return
    for num in range(1, size + 1):
        vect[idx] = num
        nested_loops(vect, idx + 1, size)


n = int(input())
vector = [None] * n
nested_loops(vector, 0, n)
