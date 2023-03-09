
def get_data(file_name):
    with open(file_name,'r') as file:
        data = file.readline().strip('\n')
        
    return data

def save_data(file,data):
    with open(file,'w') as f:
        f.write(data)


def main():
    file_name = "inputs/00-example.txt"
    
    data = get_data(file_name)
    R, C, S = tuple(map(int, data[0].split()))
    snake_lenghts = list(map(int, data[1].split()))
    matrix = [row.split() for row in data[2:]]
    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if value.isdigit():
                matrix[r][c] = int(value)
    
    
    return R, C, S, snake_lenghts, matrix
    


if __name__ == '__main__':
    main()

