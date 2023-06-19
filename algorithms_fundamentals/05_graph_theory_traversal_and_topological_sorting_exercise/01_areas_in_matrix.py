# https://judge.softuni.org/Contests/Practice/Index/3463#0

def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row, col + 1, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row - 1, col, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []
for _ in range(rows):
    matrix.append([x for x in input()])
    visited.append([False] * cols)

areas = {}
total_areas = 0
for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        node = matrix[row][col]

        dfs(node, row, col, matrix, visited)

        if node not in areas:
            areas[node] = 0
        areas[node] += 1
        total_areas += 1

print(f"Areas: {total_areas}")
for area, count in sorted(areas.items(), key=lambda x: x[0]):
    print(f"Letter '{area}' -> {count}")
