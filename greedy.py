import parsers

inf = 999999
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
move_dict = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def main():
    R, C, S, snake_lenghts, matrix = parsers.get_data()
    
    
def decide_move_best_neighbour(snake_pos, matrix, R, C):

    best_move = None
    best_score = -inf
    
    for move in moves:
        new_x, new_y = add_tuples(snake_pos, move)
        
        if new_x < 0:
            new_x = R - 1
        if new_x >= R:
            new_x = 0
        if new_y < 0:
            new_y = C - 1
        if new_y >= C:
            new_y = 0
            
        score = matrix[new_x][new_y]
        if score > best_score:
            best_move = move
            best_score = score
            
    if best_score == -inf:
        return -1, (new_x, new_y)        
    
    return move_dict[best_move], (new_x, new_y)
