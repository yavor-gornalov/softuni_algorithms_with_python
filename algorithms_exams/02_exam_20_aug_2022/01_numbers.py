# # https://judge.softuni.org/Contests/Practice/Index/3623#0

def print_combinations(n, current_combination):
    if n == 0:
        print(" + ".join(str(num) for num in current_combination))
        return

    if current_combination:
        combination_range = min(n, current_combination[-1])
    else:
        combination_range = n

    for i in range(combination_range, 0, -1):
        print_combinations(n - i, current_combination + [i])


number = int(input())
combination = []
print_combinations(number, [])
