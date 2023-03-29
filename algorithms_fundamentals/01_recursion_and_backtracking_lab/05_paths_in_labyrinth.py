# https://judge.softuni.org/Contests/Practice/Index/3459#4

def is_inner_point(puzzle, row, col):
    if row < 0 or col < 0 or row >= len(puzzle) or col >= len((puzzle[0])):
        return True
    return False


def get_all_paths(puzzle, row, col, direction, path):
    if is_inner_point(puzzle, row, col):
        return
    if puzzle[row][col] == WALL:
        return
    if puzzle[row][col] == VISITED:
        return

    path.append(direction)

    if puzzle[row][col] == EXIT:
        print("".join(path))
    else:
        puzzle[row][col] = VISITED

        get_all_paths(puzzle, row, col + 1, RIGHT, path)
        get_all_paths(puzzle, row + 1, col, DOWN, path)
        get_all_paths(puzzle, row, col - 1, LEFT, path)
        get_all_paths(puzzle, row - 1, col, UP, path)

        puzzle[row][col] = EMPTY

    path.pop()


VISITED, WALL, EXIT, EMPTY = "v", "*", "e", "-"
RIGHT, LEFT, DOWN, UP = "R", "L", "D", "U"

rows, cols = int(input()), int(input())
labyrinth = []

for _ in range(rows):
    labyrinth.append(list(input()))

get_all_paths(labyrinth, 0, 0, "", [])
