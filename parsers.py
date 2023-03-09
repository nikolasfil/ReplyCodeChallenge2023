
def get_data(file_name):
    with open(file_name,'r') as f:
        # data = file.readline().strip('\n')

        R, C, S = tuple(map(int, f.readline().strip('\n').split()))
        print(R, C, S)

        snake_lenghts = list(map(int, f.readline().strip('\n').split()))
 

        matrix = [list(map(notasterisk,f.readline().strip('\n').split())) for _ in range(R)]
        print(matrix)
    
    return R, C, S, snake_lenghts, matrix
        
def notasterisk(x):
    if x!='*':
        return int(x) 
    return '*'

def save_data(file,data):
    with open(file,'w') as f:
        f.write(data)


def main():
    file_name = "inputs/00-example.txt"
    
    R, C, S, snake_lenghts, matrix=get_data(file_name)
    
    


if __name__ == '__main__':
    main()

