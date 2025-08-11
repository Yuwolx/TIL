import sys
sys.stdin = open('input.txt')

# Purpose: print visit order in dfs and bfs
# N is number of vertex
# M is edge's number
# V is starting point
N, M, V = map(int, input().split())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    x,y = map(int, input().split())
    edges[x].append(y)
    # Because there is no direction
    edges[y].append(x)
visited = [0] * (N+1)

def dfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in edges[V]:
        if visited[i] ==0:
            dfs(i)


def bfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in edges[V]:
        if visited[i] ==0:
            dfs(i)

print(edges)
dfs(V)
bfs(V)
