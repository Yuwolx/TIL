import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    # n is box size, m is number of item
    n, m = map(int,input().split())

    items = []
    
    for _ in range(m):
        # s = size, p = price
        s, p = map(int, input().split())

        items.append([s,p])

    # max value per size
    max_val = [0 for _ in range(n+1)]

    for s, p in items:
        for i in range(n, s-1, -1):
            max_val[i] = max(max_val[i], p + max_val[i-s])

    print(f'#{tc} {max(max_val)}') 