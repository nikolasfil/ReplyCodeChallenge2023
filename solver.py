from greedy import decide_move_best_neighbour

inf = 999999

def solve(R, C, S, snake_lenghts, matrix):
    moves = [[] for _ in range(S)]

    snake_start_pos = get_snake_start_pos(matrix, S)
    snake_pos = snake_start_pos.copy()
    
    for snake in snake_start_pos:
        matrix[snake[0]][snake[1]] = -inf
        
    snake_lenghts = [x - 1 for x in snake_lenghts]
    # print(snake_start_pos)
    while any(x > 0 for x in snake_lenghts):
        for index, (curr_snake_pos, curr_snake_len) in enumerate(zip(snake_pos, snake_lenghts)):
            if not moves[index] and curr_snake_pos != snake_start_pos[index]:
                snake_lenghts[index] = 0
                continue
            if curr_snake_len <= 0:
                continue
            move, new_snake_pos = decide_move_best_neighbour(curr_snake_pos, matrix, R, C)
            # print(new_snake_pos, matrix[new_snake_pos[0]][new_snake_pos[1]])
            moves[index].append(move)
            
            if move == -1:
                moves[index] = [] 
                
            snake_pos[index] = new_snake_pos
            snake_lenghts[index] -= 1
            matrix[new_snake_pos[0]][new_snake_pos[1]] = -inf
            
        # for i in range(R):
        #     for j in range(C):
        #         print(matrix[i][j] if matrix[i][j] != -inf else "#", end=" ")
        #     print()
        # print()
            
    return snake_start_pos, moves


def get_snake_start_pos(matrix, S):
    queue = []
    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if not queue or value > queue[-1][0]:
                queue.append((value, (r, c)))
                queue.sort(key=lambda x: x[0], reverse=True)
                if len(queue) > S:
                    queue.pop()
    return [x[1] for x in queue]