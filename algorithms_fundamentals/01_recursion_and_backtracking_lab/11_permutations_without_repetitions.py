"""
Given a set of elements, find all permutations without repetitions.
Input:
    A B C
Output:
    A B C
    A C B
    B A C
    B C A
    C B A
    C A B
"""


def print_permutations(idx, vect, seq):
    if idx == len(seq):
        print(*vect, sep=" ")
        return

    for el in seq:
        if el in vect:
            continue
        vect[idx] = el
        print_permutations(idx + 1, vect, seq)
        vect[idx] = None


elements = input().split()
vector = [None] * len(elements)
print_permutations(0, vector, elements)
