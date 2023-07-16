# https://judge.softuni.org/Contests/Practice/Index/2484#0

def generate_combinations(idx, vect, seq):
    if idx == len(vect):
        return [tuple(vect)]

    combinations = []
    for el in seq:
        if el not in vect:
            vect[idx] = el
            combinations.extend(generate_combinations(idx + 1, vect, seq))
            vect[idx] = None
    return combinations


nucleus_sequence = input().split()
combinations_length = int(input())

vect = [None] * combinations_length
result = generate_combinations(0, vect, nucleus_sequence)

for combination in result:
    print(*combination, sep=" ")
