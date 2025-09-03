import sys
sys.setrecursionlimit(10000)

N = int(input())


description = [[] for _ in range(N)]
for i in range(N):
    row = input()
    for z in row:
         description[i].append(int(z))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
apt_num = 1
count_each = []

def make_group(y,x):
        global apt_count
        description[y][x] = apt_num
        for i in range(4):
            if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N:
                if description[y+dy[i]][x+dx[i]] == 1:
                    description[y+dy[i]][x+dx[i]] = apt_num
                    apt_count += 1
                    make_group(y+dy[i], x+dx[i])
        

for y in range(N):
     for x in range(N):
          if description[y][x] == 1:
               apt_count = 1
               apt_num += 1
               make_group(y,x)
               count_each.append(apt_count)
               
count_each.sort()
print(apt_num-1)
for i in count_each:
     print(i)