def solution(file):
    matrix = []
    res = 0
    for line in file:
        row = list(line.strip())
        matrix.append(row)
    a = True
    while a == True:
        a = False
        for i in range(len(matrix)):
            for j in range(len(matrix[1])):
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
                ctr = 0
                if matrix[i][j] == '.':
                    continue
                for dr in directions:
                    new_dir = [i + dr[0], j + dr[1]]
                    if not (0<= new_dir[0] < len(matrix)) or not (0<= new_dir[1] < len(matrix[1])):
                        continue
                    if matrix[new_dir[0]][new_dir[1]] == '@':
                        ctr+=1

                if ctr < 4:
                    matrix[i][j] = '.'
                    a = True
                    res += 1

    print(matrix)
    print(res)

        
with open("input.txt", 'r') as file:
    solution(file)    


