
def solution(file):
    
    res = 0 
    valid_index = 0

    for line in file:

        line = line.strip()
        prev_index = 0
        str_ans = ''
        while len(str_ans) < 12:
            max_val = 0

            for i in range(prev_index, len(line) - 12 +  len(str_ans) + 1):
                if int(line[i]) > max_val:
                    max_val = int(line[i])
                    valid_index = i

            prev_index = valid_index + 1
            str_ans += line[valid_index]

        res += int(str_ans)

    print(res)


with open("input.txt", 'r') as file:
    solution(file)    





