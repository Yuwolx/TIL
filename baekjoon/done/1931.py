N  = int(input())

times = []
for _ in range(N):
    s,e = map(int, input().split())
    times.append([e,s])
    
times.sort()

count = 0
crt = 0
for e, s in times:
    if s>= crt:
        crt = e
        count += 1

print(count)