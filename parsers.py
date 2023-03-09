# from solver import solve


def get_data(file_name):
    with open(file_name, "r") as f:
        # data = file.readline().strip('\n')

        R, C, S = tuple(map(int, f.readline().strip("\n").split()))
        # print(R, C, S)

        snake_lenghts = list(map(int, f.readline().strip("\n").split()))

        matrix = [
            list(map(notasterisk, f.readline().strip("\n").split())) for _ in range(R)
        ]
        print(matrix)

        wormholes=[]
        for y in range(R):
            for x in range(C):
                if matrix[x][y]=='*':
                    wormholes.append((x,y))


    return R, C, S, snake_lenghts, matrix,wormholes


def notasterisk(x):
    if x != "*":
        return int(x)
    return '*'
    # return -999999


def save_data(file, start_pos,moves):
    data = ""
    for snake_pos, snake_moves in zip(start_pos, moves):
        if not moves:
            data += '\n'
            continue
        
        data += f"{snake_pos[0]} {snake_pos[1]} {' '.join(snake_moves)}\n"


    with open(file, "w") as f:
        f.write(data)


def main():
    file_name = "inputs/00-example.txt"

    C, R, S, snake_lenghts, matrix, wormholes= get_data(file_name)

    print(wormholes)
    # start_pos, moves = solve(R, C, S, snake_lenghts, matrix)

    # save_data("outputs/00-example.txt", start_pos,moves)
    


if __name__ == "__main__":
    main()
