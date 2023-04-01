from random import random, randint
from copy import deepcopy
from util.interval import BlockingInterval

ALIVE = "😁"
DEAD = "💀"

board = None
interval = None


def main():
    global board, interval
    board = get_board(20)
    print(len(board))
    print_board(board)
    interval = BlockingInterval(play, 1)
    interval.start()


def play():
    global board
    board = runGeneration(board)
    print_board(board)


def runGeneration(board):
    global interval
    new_board = deepcopy(board)
    hasChanged = False
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            negs = count_negs(board, {"i": i, "j": j})
            if cell:
                newCell = 1 < negs < 4
            else:
                newCell = negs == 3
            new_board[i][j] = newCell
            if (newCell != cell):
                hasChanged = True

    if (not hasChanged):
        interval.stop()
        print("Final board, nothing changed:")
    return new_board


def count_negs(board, pos):
    negs = 0

    # the +2 in the ranges is to accomodate the exclusive nature of the last paramter in range
    for i in range(pos["i"]-1, pos["i"]+2):
        for j in range(pos["j"]-1, pos["j"]+2):
            if not is_in_range(len(board), i, j) or not board[i][j]:
                continue
            negs += 1

    return negs


def is_in_range(length, i, j):
    return 0 <= i < length and 0 <= j < length


def get_board(size=5):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            # just a weird basic calculation to get a random number based on the coords of the cell
            random_seed = (j * i) + randint(0, size+1*size+1)
            board[i].append(get_cell(random_seed))
    return board


def print_board(board):
    global ALIVE, DEAD
    output = ""
    for row in board:
        for cell in row:
            output += ALIVE if cell else DEAD
        output += "\n"
    print(output)


def get_cell(seed):
    return seed < randint(0, seed * 2) and random() > 0.5


main()
