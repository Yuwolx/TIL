import sys
sys.stdin = open('sample_input.txt')

def find_set(x):
    #if I am not root
    if arr[x] != x:
        arr[x] = find_set(arr[x])
    return arr[x]

def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        arr[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    # whole node's count is N, 
    # M is edge's info
    N, M = map(int, input().split())
    data = list(map(int, input().split()))


    arr = [i for i in range(N+1)]

    for idx in range(0, M*2, 2):
        start_node = data[idx]
        end_node = data[idx+1]
        union(start_node, end_node)

    for i in range(1, N+1):
        # find real representative
        find_set(i)

    print(f'#{tc} {len(set(arr)) -1}')

