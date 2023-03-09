
def get_data(file_name):
    with open(file_name,'r') as file:
        data = file.readline().strip('\n')
        
    return data

def save_data(file,data):
    with open(file,'w') as f:
        f.write(data)


def main():
    pass


if __name__ == '__main__':
    main()

