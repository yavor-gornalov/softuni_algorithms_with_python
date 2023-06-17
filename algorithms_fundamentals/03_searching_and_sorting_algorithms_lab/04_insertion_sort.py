# https://judge.softuni.org/Contests/Practice/Index/3461#3

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


numbers = [int(x) for x in input().split()]
numbers = insertion_sort(numbers)
print(*numbers, sep=" ")
