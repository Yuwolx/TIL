# 0,0 to N-1, M-1 (in index)
# follow 0 line
# but can break wall one time
# find least distinct route

row, col = map(int, input().split())

map = [list(map(int, input())) for _ in range(row)]

for i in map:
    print(i)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]