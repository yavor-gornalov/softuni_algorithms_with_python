# https://judge.softuni.org/Contests/Practice/Index/3460#2

def count_all_paths(row, col, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1  # Endpoint reached

    result = 0
    result += count_all_paths(row, col + 1, rows, cols)  # Right
    result += count_all_paths(row + 1, col, rows, cols)  # Left

    return result


m = int(input())
n = int(input())

print(count_all_paths(0, 0, m, n))
