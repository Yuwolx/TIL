import sys
sys.stdin = open('input.txt')

def union(s,e):
    rs = find(s)
    re = find(e)
    if rs != re:
        root[re] = rs
        return True


def find(n):
    while root[n] != n:
        root[n] = root[root[n]]
        n = root[n]
    return n


T = int(input())
for tc in range(1,T+1):
    vertex, edge = map(int,input().split())
    edges = []
    for _ in range(edge):
        s, e, w = map(int, input().split())
        edges.append([w, s,e])

    edges.sort()

    root = [i for i in range(vertex+1)]

    result = 0
    for w, s, e in edges:
        if union(s,e):
            result += w
    print(f'#{tc} {result}')


