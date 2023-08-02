"""
Given a list of elements, find all permutations.
Input:
    A B B
Output:
    A B B
    B A B
    B B A
"""
from collections import deque


def swap_elements(first_idx, second_idx, seq):
    seq[first_idx], seq[second_idx] = seq[second_idx], seq[first_idx]
    return seq


def print_permutations(seq):
    for i in range(len(seq)):
        print(*seq, sep=" ")
        seq.rotate(1)


elements = deque(input().split())
print_permutations(elements)
