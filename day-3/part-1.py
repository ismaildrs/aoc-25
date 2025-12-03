

def solution(file):
    res = 0
    for line in file:
        line = line.strip()
        mx = 0
        mx_val = 0
        for i in range(len(line)-1):
            mx = max(mx, int(line[i]))
            second_mx = 0
            for j in range(i+1, len(line)):
               second_mx = max(second_mx, int(line[j])) 
            mx_val = max(mx_val, mx * 10 + second_mx)
        res += mx_val
    print(res)

with open("input.txt", 'r') as file:
    solution(file)    



