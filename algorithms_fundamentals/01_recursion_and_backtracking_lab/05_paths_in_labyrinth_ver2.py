# https://judge.softuni.org/Contests/Practice/Index/3459#4

def find_all_paths(puzzle, row, col, path):
    if not 0 <= row < len(labyrinth):
        return
    if not 0 <= col < len(labyrinth[0]):
        return

    if puzzle[row][col] == EXIT:
        print(*path, sep="")
    elif puzzle[row][col] != EMPTY:
        return
    else:
        puzzle[row][col] = VISITED

        for direction in directions:
            path.append(direction)
            r = row + directions[direction][0]
            c = col + directions[direction][1]
            find_all_paths(puzzle, r, c, path)
            path.pop()

        puzzle[row][col] = EMPTY


VISITED, WALL, EXIT, EMPTY = "v", "*", "e", "-"
directions = {
    "R": [0, 1],
    "D": [1, 0],
    "L": [0, -1],
    "U": [-1, 0],
}

rows, cols = [int(input()) for _ in range(2)]

labyrinth = [[x for x in input()] for _ in range(rows)]

find_all_paths(labyrinth, 0, 0, [])
