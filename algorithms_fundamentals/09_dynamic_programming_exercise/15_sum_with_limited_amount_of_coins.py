def coin_available(coins_by_count):
    for coin in coins_by_count:
        if coins_by_count[coin]:
            return True
    return False


def get_combinations(coins_by_count, target, combination):
    if not coin_available(coins_by_count):
        return []
    if sum(combination) == target:
        return [tuple(sorted(combination))]  # Store sorted combinations as tuples

    unique_combinations = set()  # Use a set to store unique combinations
    for coin, count in coins_by_count.items():
        if count > 0:
            coins_by_count[coin] -= 1
            combination.append(coin)
            current_combination = get_combinations(coins_by_count, target, combination)
            unique_combinations.update(current_combination)
            combination.remove(coin)
            coins_by_count[coin] += 1
    return unique_combinations


coins = [int(x) for x in input().split()]
target = int(input())

coins_by_count = {}
result = []
for coin in coins:
    if coin not in coins_by_count:
        coins_by_count[coin] = 0
    coins_by_count[coin] += 1

result = get_combinations(coins_by_count, target, [])
combinations_count = len(result)
print(combinations_count)
