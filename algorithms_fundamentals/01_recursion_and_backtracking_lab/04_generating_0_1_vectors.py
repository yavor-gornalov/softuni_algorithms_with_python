# https://judge.softuni.org/Contests/Practice/Index/3459#3

def print_vector(vect, idx):
    if idx >= len(vect):
        print(*vect, sep="")
        return
    for num in range(2):
        vect[idx] = num
        print_vector(vect, idx + 1)


n = int(input())
vector = [0] * n

print_vector(vector, 0)
