# https://judge.softuni.org/Contests/Practice/Index/3623#0

def print_combinations(idx, combination, max_num_per_idx):
    if sum(combination) > max_num_per_idx[0]:
        return
    if sum(combination) == max_num_per_idx[0]:
        print(" + ".join(str(x) for x in combination if x > 0))
        return

    for num in range(max_num_per_idx[idx], 0, -1):
        if idx > 0 and num > combination[idx - 1]:
            continue
        combination[idx] = num
        print_combinations(idx + 1, combination, max_num_per_idx)
        combination[idx] = 0


n = int(input())

max_digit_per_index = [x for x in range(n, 0, -1)]
combination = [0] * n

print_combinations(0, combination, max_digit_per_index)
