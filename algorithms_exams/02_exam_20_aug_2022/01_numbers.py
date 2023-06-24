# https://judge.softuni.org/Contests/Practice/Index/3623#0

def find_sum_combinations(num, current_sum, numbers, combination, all_combinations):
    if num == 0:
        all_combinations.append([0])
        return
    elif current_sum == num:
        if sorted(combination, reverse=True) not in all_combinations:
            all_combinations.append(combination)
        return
    elif current_sum > num:
        return

    for n in numbers:
        new_sum = current_sum + n
        if new_sum <= num:
            new_combination = combination + [n]
            find_sum_combinations(num, new_sum, numbers, new_combination, all_combinations)


def find_all_sum_combinations(num):
    numbers = [i for i in range(num, 0, - 1)]
    combination = []  # Initialize an empty combination
    all_combinations = []
    find_sum_combinations(num, 0, numbers, combination, all_combinations)
    return all_combinations


# Example usage:
number = int(input())
results = find_all_sum_combinations(number)

for result in results:
    print(*result, sep=" + ")
