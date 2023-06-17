# https://judge.softuni.org/Contests/Practice/Index/3461#2

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


numbers = [int(x) for x in input().split()]
numbers = bubble_sort(numbers)
print(*numbers, sep=" ")
