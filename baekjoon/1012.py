# bug can move close farm
# standard of close is in against 4 direction
# How many bug need to protect agrecultures
import sys
sys.setrecursionlimit(10000)

dx = [0, 0, -1, 1] # up down left right
dy = [-1, 1, 0, 0]

def find_bc(y,x):
    farm[y][x] = result
    for i in range(0, 4):
        if  0<= y+dy[i] <row and 0 <= x+dx[i] < col:
            if farm[y+dy[i]][x+dx[i]] == 1:
                find_bc(y+dy[i],x+dx[i])

T = int(input())
for tc in range(1,T+1):
    # bc is count of baechoo
    col, row, bc = map(int, input().split())

    farm = [[0 for _ in range(col)] for _ in range(row)]

    # mark bc location
    for _ in range(bc):
        a, b = map(int, input().split())
        farm[b][a] = 1

    result = 1
    for y in range(row):
        for x in range(col):
            # when meet bc
            if farm[y][x] == 1:
                result += 1
                find_bc(y,x)

    print(result - 1)




