# https://judge.softuni.org/Contests/Practice/Index/4041#0

directions = [
    (-1, 0),  # UP
    (-1, 1),  # UP RIGHT
    (0, 1),  # RIGHT
    (1, 1),  # DOWN RIGHT
    (1, 0),  # DOWN
    (1, -1),  # DOWN LEFT
    (0, -1),  # LEFT
    (-1, -1),  # UP LEFT
]


def find_word_in_matrix(row, col, idx, current_word, target, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if idx >= len(target):
        return current_word == target

    if matrix[row][col] != target[idx]:
        return

    current_word.append(matrix[row][col])

    for r, c in directions:
        if find_word_in_matrix(row + r, col + c, idx + 1, current_word, target, matrix):
            return ''.join(target)

    current_word.pop()


rows = int(input())
cols = int(input())

grid = [list(input()) for _ in range(rows)]

words = [list(w) for w in input().split()]

unique_words = set()
for word in words:
    for r in range(rows):
        for c in range(cols):
            result = find_word_in_matrix(r, c, 0, [], word, grid)
            if result:
                unique_words.add(result)

[print(w) for w in unique_words]
