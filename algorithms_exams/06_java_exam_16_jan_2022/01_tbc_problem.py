# https://judge.softuni.org/Contests/Practice/Index/3347#0

directions = [
    (-1, 0),  # UP
    (-1, 1),  # UP RIGHT
    (0, 1),  # RIGHT
    (1, 1),  # DOWN RIGHT
    (1, 0),  # DOWN
    (1, -1),  # DOWN LEFT
    (0, -1),  # LEFT
    (-1, -1)  # UP LEFT
]


def connected_tunnels(row, col, matrix, visited):  # DFS
    if not 0 <= row < len(matrix) or not 0 <= col < len(matrix[0]):
        return 0
    if matrix[row][col] != "t":
        return 0
    if visited[row][col]:
        return 0

    visited[row][col] = True

    for r, c in directions:
        connected_tunnels(row + r, col + c, matrix, visited)

    return 1


rows = int(input())
cols = int(input())

city_map = []
visited = []
for _ in range(rows):
    city_map.append([x for x in input()])
    visited.append([False] * cols)

result = 0
for i in range(rows):
    for j in range(cols):
        if city_map[i][j] != "t":
            continue
        if visited[i][j]:
            continue
        result += connected_tunnels(i, j, city_map, visited)

print(result)
