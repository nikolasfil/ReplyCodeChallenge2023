from solver import solve


def get_data(file_name):
    with open(file_name, "r") as f:
        # data = file.readline().strip('\n')

        C, R, S = tuple(map(int, f.readline().strip("\n").split()))
        print(R, C, S)

        snake_lenghts = list(map(int, f.readline().strip("\n").split()))

        matrix = [
            list(map(notasterisk, f.readline().strip("\n").split())) for _ in range(R)
        ]
        # print(matrix)

    return R, C, S, snake_lenghts, matrix


def notasterisk(x):
    if x != "*":
        return int(x)
    # return '*'
    return -999999


def save_data(file, data):
    with open(file, "w") as f:
        f.write(data)


def main():
    files = ["inputs/00-example.txt",
             "inputs/01-chilling-cat.txt",
             "inputs/02-swarming-ant.txt",
             "inputs/03-input-anti-greedy.txt",
            #  "inputs/04-input-low-points.txt",
             "inputs/05-input-opposite-points-holes.txt"]
    for file_name in files:
        R, C, S, snake_lenghts, matrix = get_data(file_name)

        start_pos, moves = solve(R, C, S, snake_lenghts, matrix)

        data = ""
        for snake_pos, snake_moves in zip(start_pos, moves):
            # print(snake_moves)
            if not snake_moves:
                data += '\n'
                continue
            # print(snake_moves)
            data += f"{snake_pos[1]} {snake_pos[0]} {' '.join(snake_moves)}\n"

        save_data(f"outputs/{file_name.split('/')[1]}", data)


if __name__ == "__main__":
    main()
