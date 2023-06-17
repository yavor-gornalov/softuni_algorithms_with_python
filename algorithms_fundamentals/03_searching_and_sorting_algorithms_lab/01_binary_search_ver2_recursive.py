# https://judge.softuni.org/Contests/Practice/Index/3461#0

def binary_search_recursive(nums, left_idx, right_idx, target):
    if left_idx > right_idx:
        return -1

    middle_idx = (left_idx + right_idx) // 2
    middle_el = nums[middle_idx]
    if middle_el == target:
        return middle_idx
    elif middle_el > target:
        return binary_search_recursive(nums, left_idx, middle_idx - 1, target)
    else:
        return binary_search_recursive(nums, middle_idx + 1, right_idx, target)


numbers = sorted(int(x) for x in input().split())
searched_number = int(input())
print(binary_search_recursive(numbers, 0, len(numbers) - 1, searched_number))
