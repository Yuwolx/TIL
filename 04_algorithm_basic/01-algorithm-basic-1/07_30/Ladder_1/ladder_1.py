import sys
# open input text file
sys.stdin = open('input.txt', 'r')

    #left right down
dx = [-1, 1, 0]
dy = [0, 0, 1]

# explore to destination
def explore(col):
    # check whether visit
    visited = [[0] * 100 for _ in range(100)]

    row = 0
    # starting point
    visited[row][col] = 1

    # keep going to 99
    while row != 99:
        # priority address side direction
        for dir in range(3):
            next_col = col + dx[dir]
            next_row = row + dy[dir]
            
            # check next point in ladder
            if 0<= next_col < 100 and 0 <= next_row < 100:
                #chect there is load
                if ladder[next_row][next_col] != 0:
                    # check, it is finish point
                    if ladder[next_row][next_col] == 2:
                        return True
                    # check visited before
                    if visited[next_row][next_col] == 0:
                        # move
                        row, col = next_row, next_col
                        # check visit
                        visited[row][col] = 1
                        continue
    return False




# given 10 test case
for _ in range(10):
    test_case = int(input())

    #make ladder 
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # starting points
    candidates = []
    start_low = ladder[0]
    for i in range(len(start_low)):
        if start_low[i]:
            candidates.append(i)

    # find from starting point
    for pt in candidates:
        if explore(pt):
            break

    print(f'#{test_case} {pt}')