import sys
sys.stdin = open('re_sample_input.txt')

def link_island(xs,ys):
    N = len(xs)
    min_len = 10**30

    # Check whether visited or not
    visited = [False] * N

    min_cost = [min_len] * N
    min_cost[0] = 0

    total_fee = 0

    for _ in range(N):
        # find min cost in not visited vertex
        u = -1
        m = min_len
        for i in range(N):
            if not visited[i] and min_cost[i] < m:
                m = min_cost[i]
                u = i
        visited[u] = True
        total_fee += m

        ux, uy = xs[u], ys[u] 
        for v in range(N):
            if not visited[v]:
                dx = ux - xs[v]
                dy = uy - ys[v]
                w = dx*dx + dy*dy
                if w < min_cost[v]:
                    min_cost[v] = w
    return total_fee


T = int(input())
for tc in range(1, T+1):
    # Number of islands
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    # tax rate
    E = float(input())


    total_fee = link_island(X,Y)

    result = round(total_fee*E)

    print(f'#{tc} {result}')