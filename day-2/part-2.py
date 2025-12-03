

def solution(file):
    sm = 0

    inp = file.readline().strip('\n')
    arr = [tuple(i.split("-")) for i in inp.split(",")]

    for s, f in arr:
        for v in range(int(s), int(f)+1):
            s = str(v)
            for i in range(1, len(s)//2+1):
                elem = s[:i]
                a = False
                for j in range(i, len(s), i):
                    if elem != s[j:j+i]:
                        break
                    elem = s[j:j+i]
                else:
                    a = True
                if a: 
                    sm += v
                    break

    print(sm)

with open("input.txt", 'r') as file:
    solution(file)    


