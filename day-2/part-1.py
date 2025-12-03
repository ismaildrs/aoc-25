

def solution(file):

    inp = file.readline().strip('\n')
    arr = [tuple(i.split("-")) for i in inp.split(",")]

    sm = 0

    for s, f in arr:
        for i in range(int(s), int(f)):
            s = str(i)
            if s[:len(s)//2] == s[len(s)//2:]:
                print(s)
                sm += i            

    print(sm)

with open("input.txt", 'r') as file:
    solution(file)    




