import sys
sys.stdin = open('input.txt')

from collections import deque

# Purpose: print visit order in dfs and bfs
# N is number of vertex
# M is edge's number
# V is starting point
N, M, V = map(int, input().split())

edges = [[] for _ in range(N + 1)]

def dfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in edges[V]:
        if not visited[i]:
            dfs(i)


def bfs(V):
    plans = deque([V])
    visited[V] = 1
    while plans:
        V = plans.popleft()
        print(V, end= ' ')
        for i in edges[V]:
            if not visited[i]:
                plans.append(i)
                visited[i] = 1




for _ in range(M):
    x,y = map(int, input().split())
    edges[x].append(y)
    # Because there is no direction
    edges[y].append(x)

for i in edges:
    i.sort()

visited = [0] * (N+1)
dfs(V)
print()
visited = [0] * (N+1)

bfs(V)
