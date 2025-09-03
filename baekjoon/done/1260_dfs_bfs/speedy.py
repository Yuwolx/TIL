import sys
sys.stdin = open('input.txt')

from collections import deque

N, M, s = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

for lit in edges:
    lit.sort()

visited = [False] * (N+1)
def dfs(s):
    visited[s] = 1
    print(s, end =' ')
    for i in edges[s]:
        if not visited[i]:
            dfs(i)

dfs(s)
print()

visited = [False] * (N+1)
def bfs(s):
    plans = deque()
    visited[s] = 1
    plans.append(s)
    while plans:
        s = plans.popleft()
        print(s, end=' ')
        for i in edges[s]:
            if not visited[i]:
                visited[i] = 1
                plans.append(i)

bfs(s)