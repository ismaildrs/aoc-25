def solution(file):
    arr = []

    for fline in file:
        op = fline[0]
        val = int(fline[1:])
        arr.append(val * (-1 if op == "L" else 1))

    dial = 50
    ctr = 0

    for v in arr:
        rest = abs(v) % 100

        if v < 0:
            dial -= rest 
        else:
            dial += rest

        dial = dial % 100


        if dial == 0: ctr += 1


    print(ctr)
 

with open("input.txt", 'r') as file:
    solution(file)    


