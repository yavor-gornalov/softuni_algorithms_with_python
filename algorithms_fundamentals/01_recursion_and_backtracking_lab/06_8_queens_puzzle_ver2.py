# https://judge.softuni.org/Contests/Practice/Index/3459#5

QUEEN, FREE = "*", "-"
BOARD_SIZE = 8


def print_board(board):
    for i in range(BOARD_SIZE):
        print(*board[i], sep=" ")
    print()


def put_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    chessboard[row][col] = QUEEN
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    chessboard[row][col] = FREE
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def is_queen_position_attacked(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows:
        return True
    if col in cols:
        return True
    if row - col in left_diagonals:
        return True
    if row + col in right_diagonals:
        return True
    return False


def put_queens(board, row, rows, cols, left_diagonals, right_diagonals):
    if row == BOARD_SIZE:
        print_board(board)
        return

    for col in range(BOARD_SIZE):
        if not is_queen_position_attacked(row, col, rows, cols, left_diagonals, right_diagonals):
            put_queen(row, col, rows, cols, left_diagonals, right_diagonals)
            put_queens(board, row + 1,  rows, cols, left_diagonals, right_diagonals)
            remove_queen(row, col, rows, cols, left_diagonals, right_diagonals)


chessboard = [[FREE] * 8 for _ in range(BOARD_SIZE)]
put_queens(chessboard, 0, set(), set(), set(), set())
