# https://judge.softuni.org/Contests/Practice/Index/3461#0

def binary_search(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if nums[middle_idx] == target:
            return middle_idx

        if target < nums[middle_idx]:
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1

    return -1


numbers = [int(x) for x in input().split()]
searched_number = int(input())
print(binary_search(sorted(numbers), searched_number))
