import sys
sys.stdin = open('sample_input.txt')

from collections import deque

# def store(n, idx):
#     if idx == 0:
#         return
#     need.append([n-1,idx])
#     need.append([n-1,idx - 1])
#     store(n-1,idx -1)




        
        
        
def evaluation(n, idx):
    if idx == 0:
        return 1
    elif idx == 1:
        return n

    else:
        if idx == n/2:
            return arr[n-1][idx - 1] * 2
        else:
            return arr[n-1][idx] + arr[n-1][idx - 1]
        

T = int(input())
for tc in range(1,T+1):
    n, a, b = map(int, input().split())
    if a >= b:
        idx = b
    else:
        idx = a

    arr = [[1]*(n//2+1) for _ in range(n+1)]
    # print(f'arr: {arr}')
    need = deque()
    
    # store(n, idx)

    for i in range(2, n):
        for idx in range(1,idx+1):
            need.append([i,idx])

    # print(f'need: {need}')
    # print(n, idx)

    while need:
        k = need.popleft()
        if k[1] == 1:
            arr[k[0]][k[1]] = k[0]
        elif k[1] == 0:
            arr[k[0]][k[1]] = 1
        else:
            if k[1] == k[0]/2: 
                arr[k[0]][k[1]] = arr[k[0]-1][k[1]-1] * 2
            else:
                arr[k[0]][k[1]] = arr[k[0]-1][k[1]-1] + arr[k[0]-1][k[1]]

        # print(f'arr: {arr}')

    result = evaluation(n,idx)

    print(f'#{tc} {result}')
    # print()




