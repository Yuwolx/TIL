import sys
sys.stdin = open('input.txt')

# idea
# basically number's order is the same as order of explore tree by in order
# so explore tree and insert value from 1 in same tiom

def inorder(index):
    global value
    # when index more small then max idx
    if index <= N:
        #find left child
        inorder(index*2)
        tree[index] = value
        value += 1
        #find right child
        inorder(index*2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #because 0 index not use
    tree = [0] * (N+1)
    value = 1
    inorder(1)
    print(f'#{tc}', end = ' ')
    print(tree[1], end = ' ')
    print(tree[N//2])