# https://judge.softuni.org/Contests/Practice/Index/3459#5
"""
TODO: Not finished, yet
"""
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def set_attacked_fields(board, queen_row, queen_coll, symbol):
    board[queen_row] = [symbol] * SIZE
    for r in range(queen_row, SIZE):
        board[r][queen_coll] = symbol
    r, c = queen_row, queen_coll
    while r < SIZE and c < SIZE:
        board[r][c] = symbol
        r += 1
        c += 1
    r, c = queen_row, queen_coll
    while r < SIZE and c >= 0:
        board[r][c] = symbol
        r += 1
        c -= 1


def is_set_queen_possible(board, row, col): return board[row][col] == FREE


def set_queen(board, row, col):
    set_attacked_fields(board, row, col, ATTACKED)
    board[row][col] = QUEEN


def reset_queen(board, row, col):
    set_attacked_fields(board, row, col, FREE)


def put_queens(board, row):
    if row >= SIZE:
        print_board(board)
        return
    for col in range(SIZE):
        if is_set_queen_possible(board, row, col):
            set_queen(board, row, col)
            put_queens(board, row + 1)
            reset_queen(board, row, col)


SIZE = 8
QUEEN, FREE, ATTACKED = "*", "-", "+"
chessboard = []
[chessboard.append([FREE] * SIZE) for _ in range(SIZE)]

put_queens(chessboard, 0)
