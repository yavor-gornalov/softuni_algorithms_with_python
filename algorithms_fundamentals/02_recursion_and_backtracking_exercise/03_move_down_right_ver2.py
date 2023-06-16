# https://judge.softuni.org/Contests/Practice/Index/3460#2

def possible_paths(row, col, end_row, end_col):
    if row >= end_row or col >= end_col:
        return 0
    if row == end_row - 1 and col == end_col - 1:
        return 1
    result = 0
    result += possible_paths(row, col + 1, end_row, end_col)
    result += possible_paths(row + 1, col, end_row, end_col)
    return result


rows = int(input())
cols = int(input())
paths_count = possible_paths(0, 0, rows, cols)
print(paths_count)
