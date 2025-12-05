def solution(file):
    arr = []
    for line in file:
        line = line.strip()
        if line == "":
            break
        arr.append([int (i) for i in line.split("-")])
            
    arr.sort()
    i = 1
    while i < len(arr):
        if arr[i][0] <= arr[i-1][1]:
            if(arr[i][1]>=arr[i-1][1]):
                arr[i-1][1]=arr[i][1]
            arr.pop(i)
            i-=1
        i+=1
    ctr = 0
    for s, e in arr:
        ctr += (e - s + 1)

    print(ctr)

with open("input.txt", 'r') as file:
    solution(file)    


