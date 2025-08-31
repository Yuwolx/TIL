n = int(input())

triangle = []
for i in range(n):
    triangle.append(list(map(int,input().split())))

cal= []
for i in range(1,n+1):
    cal.append([0 for _ in range(i)])



cal[0] = triangle[0]


for y in range(0,n-1):
    # sum
    for x in range(y+1):
        cal[y+1][x] = max(cal[y][x] + triangle[y+1][x], cal[y+1][x])
        cal[y+1][x+1] = max(cal[y][x] + triangle[y+1][x+1], cal[y+1][x+1])

'''
0 -> 0 1
1 -> 1 2
2 -> 2 3
'''

result = max(cal[n-1])
print(result)

#fibonacci

n = 10

fibo = [0 for _ in range(n+1)]

fibo[1] = 1
for x in range(2,n+1):
    fibo[x] = fibo[x-1] + fibo[x-2]

print(fibo[n])