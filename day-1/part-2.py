

def solution(file):
    arr = []

    for fline in file:
        op = fline[0]
        val = int(fline[1:])
        arr.append(val * (-1 if op == "L" else 1))
        # arr.append(val)

    dial = 50
    ctr = 0

    for v in arr:
        rest = abs(v) % 100
        old_dial = dial

        if v < 0:
            dial -= rest 
        else:
            dial += rest

        if not (0 <= dial <=100) and old_dial != 0:
            ctr += 1

        ctr += abs(v) // 100
        dial = dial % 100


        if dial == 0:
            ctr += 1


    print(ctr)
 

with open("input.txt", 'r') as file:
    solution(file)    

