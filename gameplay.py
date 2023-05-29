from colors import *


def display_board(board):
    b = LIGHT_GRAY + BOLD + "  a b c d e f g h \n" + END
    r = 0
    c = 8
    for i in range(0, len(board)):
        if r == 0:
            b += LIGHT_GRAY + BOLD + str(c) + END
            c -= 1
        r += 1
        if r == 9:
            r = 0
        if board[i].isupper():
            b += " " + board[i]
        elif board[i] == ".":
            b += LIGHT_WHITE + " ." + END
        else:
            b += BLACK + " " + board[i].upper() + END
    print(b)
