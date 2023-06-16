# https://judge.softuni.org/Contests/Practice/Index/3460#3

def find_all_areas(mtx, row, col):
    if row < 0 or col < 0 or row >= len(mtx) or col >= len(mtx[0]):
        return 0
    if mtx[row][col] != EMPTY:
        return 0

    result = 1
    mtx[row][col] = VISITED

    result += find_all_areas(mtx, row + 1, col)
    result += find_all_areas(mtx, row - 1, col)
    result += find_all_areas(mtx, row, col + 1)
    result += find_all_areas(mtx, row, col - 1)

    return result


EMPTY, WALL, VISITED = "-", "*", "v"

rows = int(input())
cols = int(input())

matrix = [[x for x in input()] for _ in range(rows)]

areas = {}
for r in range(rows):
    for c in range(cols):
        area = find_all_areas(matrix, r, c)
        if area:
            areas[(r, c)] = area

print(f"Total areas found: {len(areas)}")

idx = 1
for area, size in sorted(areas.items(), key=lambda x: (-x[1], x[0])):
    print(f"Area #{idx} at {area}, size: {size}")
    idx += 1
