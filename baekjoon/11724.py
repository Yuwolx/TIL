from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)


vertexs = deque([i for i in range(1,n+1)])
visited = [False] * (n+1)
result = 0

def find_group(s):
    visited[s] = 1
    for i in edges[s]:
        if not visited[i]:
            find_group(i)

while vertexs:
    s = vertexs.popleft()
    if not visited[s]:
        find_group(s)
        result += 1

print(result)

