import sys
sys.stdin = open("input.txt", "r")


tc = 10


for i in range(tc):
    case = int(input())

    #make maze on list
    maze = []
    for s in range(16):
       line = list(map(int, input()))
       maze.append(line)

    # find start point
    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                start_y, start_x = y, x


    direction_y = [0, -1, 0, 1] # right, down, left, up
    direction_x = [1, 0, -1, 0]

    # make board to check whether visitied or not
    visited = [[False]*16 for _ in range(16)]


    def mz_dfs(y,x):
        # if find 3, close function
        if maze[y][x] == 3:
            return True
        
        visited[y][x] = True

        for d in range(4): # searching each direction, in order direction list index
            ny = y + direction_y[d]
            nx = x + direction_x[d]

            if 0 <= ny < 16 and 0 <= nx < 16:   # check next point in maze
                if not visited[ny][nx]:         # check where is already visit
                    if maze[ny][nx] == 0 or maze[ny][nx] == 3:
                        if mz_dfs(ny,nx):
                            return True

    if mz_dfs(start_y, start_x): #if function say true
        print(f"#{case} 1")
    else:
        print(f"#{case} 0")