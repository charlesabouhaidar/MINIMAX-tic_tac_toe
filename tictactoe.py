"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX, numO = 0, 0
    for i in board:
        for j in i:
            if j == X:
                numX += 1
            elif j == O:
                numO += 1

    if numO < numX:
        return O
    elif not terminal(board) and numX == numO:
        return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.add((i, j))

    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError("GAME OVER")
    elif action not in actions(board):
        raise ValueError("Impossible move")
    else:
        p = player(board)
        res = copy.deepcopy(board)
        (i, j) = action
        res[i][j] = p

    return res


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] is not None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] is not None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] is not None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] is not None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] is not None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] is not None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] is not None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] is not None:
        if board[0][2] == X:
            return X
        else:
            return O

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champion = winner(board)
    if champion == X:
        return 1
    elif champion == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == [[EMPTY] * 3] * 3:
        return 0, 0

    p = player(board)

    if p == X:
        val = float("-inf")
        move = None
        for i in actions(board):
            minValueResult = minValue(result(board, i))
            if minValueResult > val:
                val = minValueResult
                move = i
    elif p == O:
        val = float("inf")
        move = None
        for i in actions(board):
            maxValueResult = maxValue(result(board, i))
            if maxValueResult < val:
                val = maxValueResult
                move = i

    return move


def minValue(board):
    if terminal(board):
        return utility(board)
    a = float("inf")
    for i in actions(board):
        a = min(a, maxValue(result(board, i)))

    return a


def maxValue(board):
    if terminal(board):
        return utility(board)
    a = float("-inf")
    for i in actions(board):
        a = max(a, minValue(result(board, i)))

    return a
