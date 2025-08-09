import sys
sys.stdin = open('input.txt')

def inorder(node):
    node = int(node)
    if node:
        # find left child
        inorder(data[node][2])
        print(data[node][1], end = '')
        inorder(data[node][3])



for tc in range(1,11):
    N = int(input())
    data = [input().split() for _ in range(N)]
    data.insert(0, None)

    for idx in range(1, N + 1):
        while len(data[idx]) < 4:
            data[idx].append('0')
    
    print(f'#{tc}' , end = ' ')
    inorder(1)
    # change line
    print()