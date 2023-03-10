import parsers

def main():
    files = ["inputs/00-example.txt",
             "inputs/01-chilling-cat.txt",
             "inputs/02-swarming-ant.txt",
             "inputs/03-input-anti-greedy.txt",
             "inputs/04-input-low-points.txt",
             "inputs/05-input-opposite-points-holes.txt",
             "inputs/06-input-reply-running-man.txt"
            ]
    
    for f in files:
        R, C, S, snake_lenghts, matrix = parsers.get_data(f)
        
        wormholes=[]
        for x in range(R):
            for y in range(C):
                if matrix[x][y]==-999999:
                    wormholes.append((x,y))

        snake_rows = [-1 for _ in range(S)]

        for wormhole in wormholes:
            if wormhole[0] in snake_rows:
                continue
            for i, snake_len in enumerate(snake_lenghts):
                if snake_len < wormhole[1] and snake_rows[i] == -1:
                    snake_rows[i] = wormhole[0]
                    break
        # print(snake_rows)
        row = 0
        data = ""
        for i, snake_len in enumerate(snake_lenghts):
            if snake_len >= C:
                data += "\n"
                continue
            if snake_rows[i] != -1:
                data += f"{0} {snake_rows[i]} "
                for _ in range(snake_len - 2):
                    data += "R "
                data += "R\n"
                continue
            
            while row in snake_rows:
                row += 1
            if row >= R:
                data += "\n"
                continue
            data += f"{0} {row} "
            for _ in range(snake_len - 2):
                data += "R "
            data += "R\n"
            row += 1
        
        parsers.save_data(f"outputs/quick_{f.split('/')[1]}", data)
                
if __name__ == "__main__":
    main()
            
        
