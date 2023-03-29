# https://judge.softuni.org/Contests/Practice/Index/3460#3

def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] == "*" or matrix[row][col] == "v":
        return 0

    result = 1
    matrix[row][col] = "v"
    result += explore_area(row + 1, col, matrix)  # down
    result += explore_area(row, col + 1, matrix)  # right
    result += explore_area(row - 1, col, matrix)  # up
    result += explore_area(row, col - 1, matrix)  # left

    return result


rows = int(input())
cols = int(input())
array = [list(input()) for _ in range(rows)]

areas = []
for r in range(rows):
    for c in range(cols):
        size = explore_area(r, c, array)
        if not size:
            continue
        areas.append((r, c, size))

print(f"Total areas found: {len(areas)}")
for idx, area in enumerate(sorted(areas, key=lambda a: a[2], reverse=True)):
    print(f"Area #{idx + 1} at ({area[0]}, {area[1]}), size: {area[2]}")
