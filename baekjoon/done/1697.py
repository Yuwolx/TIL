from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n-k)
else:

    max = 100000
    dist = [-1] * (max+1)
    dist[n]= 0
    qu = deque([n])

    while qu:
        x = qu.popleft()
        if x == k:
            print(dist[x])
            break

        for nx in [x-1,x+1,x*2]:
            if 0<= nx <= max and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                qu.append(nx)