

# def right_to_left(arr, k):
#     tmp = []
#     for i in range(len(arr) - 1):
#         tmp.append(arr[i][k])
#     max_len = len(max(tmp))
#     res = []
#     for i in range(max_len+1):
#         number = ''
#         for j in range(len(tmp)):
#             if tmp[j]:
#                 number += tmp[j][0]
#                 tmp[j] = tmp[j][1:]
#         res.append(number)
#
#     return res
#
def do_operation(arr, operation):
    res = 1
    for i in range(len(arr)):
        if operation == '-': res -= int(arr[i])
        if operation == '+': res += int(arr[i])
        if operation == '*': res *= int(arr[i])
        if operation == '/': res /= int(arr[i])
    if operation in ['-', '+']: res -= 1
    return res

def solution(file):
    res = 0 
    lines = file.readlines()
    max_line = len(max(lines))-1

    arr = []
    index = 0
    operations = []
    for i in range(max_line-1, -1, -1):
        number = ''
        for j in range(len(lines)-1):
            line = lines[j]
            if len(line) > i and line[i] != " ": 
                number += line[i]
        if not number:
            index += 1
        else:
            if len(arr)<=index:
                arr.append([])
            arr[index].append(number)

    operations = lines[-1].strip().split()
    operations = operations[::-1]
    for k in range(len(operations)):
        res += do_operation(arr[k],operations[k])
    
    print(res)

with open("input.txt", 'r') as file:
    solution(file)    


