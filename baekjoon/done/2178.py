from collections import deque
row, col = map(int, input().split())
maze = [list(map(int, input())) for _ in range(row)]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

plans = deque()

plans.append([0,0])
maze[0][0] = 2

while plans:
    spot = plans.popleft()
    y = spot[0]
    x = spot[1]
    # end condition: reache out destination
    if spot == [row-1,col-1]: break
    for i in range(4):
        if 0 <= y+dy[i] < row and 0 <= x+dx[i] < col:
            if maze[y+dy[i]][x+dx[i]] == 1:
                maze[y+dy[i]][x+dx[i]] = maze[y][x] + 1
                plans.append([y+dy[i],x+dx[i]])


print(maze[y][x]-1)