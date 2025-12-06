

def solution(file):
    empty_line = False

    ctr = 0
    intervals = []
    for line in file:
        line = line.strip()
        if not empty_line:
            if line == "":
                empty_line = True
                continue
            intervals.append([int (v) for v in line.split("-")])
        else:
            value = int(line)
            for s, e in intervals:
                if value in range(s, e+1):
                    ctr += 1
                    break

    print(ctr)

with open("input.txt", 'r') as file:
    solution(file)    

