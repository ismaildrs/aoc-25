import re

arr = []

def right_to_left(arr, k):
    tmp = []
    for i in range(len(arr) - 1):
        tmp.append(arr[i][k])
    print(max(tmp))

def do_operation(arr, k, operation):
    res = 1
    right_to_left(arr, k)
    for i in range(len(arr)-1):
        if operation == '-': res -= int(arr[i][k])
        if operation == '+': res += int(arr[i][k])
        if operation == '*': res *= int(arr[i][k])
        if operation == '/': res /= int(arr[i][k])
    if operation in ['-', '+']: res -= 1
    return res

def solution(file):
    res = 0
    for line in file:
        line = line.strip()
        arr.append(re.split(r'(?<!\s)\s(?!\s)', line))

    print(arr)
    for k in range(len(arr[-1])):
        res += do_operation(arr, k, arr[-1][k])
    
    print(res)

with open("input.txt", 'r') as file:
    solution(file)    

