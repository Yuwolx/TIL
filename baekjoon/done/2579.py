stair = int(input())

point = [0]

for _ in range(stair):
    x = int(input())
    point.append(x)

#print(stair, point)

cal = [[0,0] for _ in range(stair+1)]


cal[1] = [point[1],point[1]]

for x in range(2,stair+1):
    cal[x] = [cal[x-1][1] + point[x], max(cal[x-2][0] + point[x],cal[x-2][1] + point[x] )]

result = max(cal[stair])
print(result)