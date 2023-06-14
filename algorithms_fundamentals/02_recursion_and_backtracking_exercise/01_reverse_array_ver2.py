# https://judge.softuni.org/Contests/Practice/Index/3460#0

def reverse_array(arr):
    if not arr:
        return
    print(arr.pop(), end=" ")
    reverse_array(arr)


array = input().split()
reverse_array(array)
