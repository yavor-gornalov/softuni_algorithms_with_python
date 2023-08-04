# https://judge.softuni.org/Contests/Practice/Index/3346#0

def print_permutations(idx, vect, seq):
    if idx == len(vect):
        print(*vect, sep=" ")
        return

    for el in seq:
        if el in vect:
            continue
        if vect and vect[idx - 1] > el:
            continue
        vect[idx] = el
        print_permutations(idx + 1, vect, seq)
        vect[idx] = -1


def generate_subsets(nums):
    for length in range(1, len(nums) + 1):
        print_permutations(idx=0, vect=[-1] * length, seq=nums)


numbers = [int(x) for x in input().split(", ")]

generate_subsets(numbers)
