# https://judge.softuni.org/Contests/Practice/Index/3623#0

def print_combinations(idx, combination, sum_combination, max_num_per_idx):
    if sum_combination > max_num_per_idx[0]:
        return
    if sum_combination == max_num_per_idx[0]:
        print(" + ".join(str(x) for x in combination if x > 0))
        return

    for num in range(max_num_per_idx[idx], 0, -1):
        if idx > 0 and num > combination[idx - 1]:
            continue
        combination[idx] = num
        sum_combination += num
        print_combinations(idx + 1, combination, sum_combination, max_num_per_idx)
        combination[idx] = 0
        sum_combination -= num


n = int(input())

print_combinations(0,
                   [0] * n,
                   0,
                   [x for x in range(n, 0, -1)])
