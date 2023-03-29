# https://judge.softuni.org/Contests/Practice/Index/3459#0

def array_sum(arr, idx):
    if idx >= len(arr) - 1:
        return arr[idx]
    return arr[idx] + array_sum(arr, idx + 1)


array = [int(x) for x in input().split()]

print(array_sum(array, 0))
