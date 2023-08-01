presents = [int(x) for x in input().split()]
total_sum = sum(presents)
sums = [0] + [-1] * total_sum

for curr_idx in range(len(presents)):
    for prev_idx in range(total_sum - presents[curr_idx], -1, -1):
        present_value = presents[curr_idx]

        if sums[prev_idx] != -1 and sums[prev_idx + present_value] == -1:
            sums[prev_idx + present_value] = curr_idx

idx = total_sum // 2
while idx == -1:
    idx -= 1

print(f"Difference: {total_sum - 2 * idx}")
print(f"Alan:{idx} Bob:{total_sum - idx}")
print("Alan takes:", end=" ")

while idx:
    print(presents[sums[idx]], end=" ")
    idx -= presents[sums[idx]]
print()
print("Bob takes the rest.")
