import math

PLAYER = 'X'
AI = 'O'
EMPTY = ''

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def is_moves_left(b):
    return any(cell == EMPTY for row in b for cell in row)

def evaluate(b):
    for row in b:
        if row[0] == row[1] == row[2] != EMPTY:
            return 10 if row[0] == AI else -10

    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != EMPTY:
            return 10 if b[0][col] == AI else -10

    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return 10 if b[0][0] == AI else -10
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return 10 if b[0][2] == AI else -10

    return 0

def minimax(b, depth, is_max, alpha, beta):
    score = evaluate(b)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    best = max(best, minimax(b, depth + 1, False, alpha, beta))
                    b[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = PLAYER
                    best = min(best, minimax(b, depth + 1, True, alpha, beta))
                    b[i][j] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI
                move_val = minimax(b, 0, False, -math.inf, math.inf)
                b[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move
