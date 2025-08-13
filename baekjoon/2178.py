from collections import deque
row, col = map(int, input().split())
maze = [list(map(int, input())) for _ in range(row)]

for r in maze:
    print(r)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

plans = deque()

