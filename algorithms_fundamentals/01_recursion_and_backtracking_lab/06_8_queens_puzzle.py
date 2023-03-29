# https://judge.softuni.org/Contests/Practice/Index/3459#5

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonals:
        return False
    if (row + col) in right_diagonals:
        return False
    return True


def set_queen(board, row, col, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = "*"
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(board, row, col, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def put_queens(board, row, rows, cols, left_diagonals, right_diagonals):
    if row >= N:
        print_board(board)
        return
    for col in range(N):
        if can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
            set_queen(board, row, col, rows, cols, left_diagonals, right_diagonals)
            put_queens(board, row + 1, rows, cols, left_diagonals, right_diagonals)
            remove_queen(board, row, col, rows, cols, left_diagonals, right_diagonals)


N = 8
chess_board = []
[chess_board.append(['-'] * N) for _ in range(N)]

put_queens(chess_board, 0, set(), set(), set(), set())
