# https://judge.softuni.org/Contests/Practice/Index/3346#0

def generate_subsets(nums, solution, result):
    result.append(solution)
    for idx in range(len(nums)):
        generate_subsets(nums[idx + 1:], solution + [nums[idx]], result)


numbers = [int(x) for x in input().split(", ")]

result = []
generate_subsets(numbers, [], result)

for line in sorted(result, key=len):
    print(" ".join(str(d) for d in line))
