import parsers
from greedy import decide_move_best_neighbour

inf = 999999

def solve(R, C, S, snake_lenghts, matrix):
    moves = [[] for _ in range(S)]

    snake_pos = get_snake_start_pos()
    for index, curr_snake_pos, curr_snake_len in enumerate(zip(snake_pos, snake_lenghts)):
        if curr_snake_len <= 0:
            continue
        move, new_snake_pos = decide_move_best_neighbour(curr_snake_pos, matrix, R, C)
        snake_pos[index] = new_snake_pos
        snake_lenghts[index] -= 1
        matrix[new_snake_pos[0]][new_snake_pos[1]] = -inf
        
        moves[index].append(move)
    return moves


def get_snake_start_pos():
    pass