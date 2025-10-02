from collections import deque

m,n = map(int, input().split())
# print(f'm,n:{m,n}')

box = []
for _ in range(n):
    i = list(map(int,input().split()))
    box.append(i)
    
# for x in box:
#     print(x)
    
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
plans = deque([])
for y in range(n):
        for x in range(m):
            if box[y][x] == 1:
                plans.append([y,x,1])

while plans:
    y,x, day = plans.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < m:
            if box[ny][nx] == 0:
                box[ny][nx] = day
                plans.append([ny,nx,day+1])
        
# for x in box:
#     print(x)
    
scs = True
for y in range(n):
    for x in range(m):
        if box[y][x] == 0:
            print(-1)
            scs = False
            exit()
        
if scs:
    print(day-1)