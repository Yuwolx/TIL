import sys
sys.stdin = open("input.txt", "r")

# Assigned test case
TC = 10
for tc in range(1, TC + 1):
    # Receive number of nodes
    N = int(input())
    # Make tree list
    tree = [0] * (N + 1)
    left = [0] * (N + 1) # List for store left child idx
    right = [0] * (N + 1)

    for _ in range(N):
        # Take node data
        nodes = input().split()
        idx = int(nodes[0])
        # Insert node value to tree as index
        tree[idx] = nodes[1]
        if len(nodes) == 4: # mean have children
            left[idx] = int(nodes[2]) # store left child's index number where the same index with parent in list
            right[idx] = int(nodes[3])

    operator = ["*", "/", "+", "-"]

    # Definition evaluate function
    def calculate(x, op, y):
        if op == '+': return x + y
        if op == '-': return x - y
        if op == '*': return x * y
        if op == '/': return x // y

    # Definition postorder func
    def postorder_eval(idx):
        val = tree[idx]
        # When function meet operator
        if val in operator:
            l = postorder_eval(left[idx])
            r = postorder_eval(right[idx])
            return calculate(l, val, r)
        else:
            return int(val)

    print(f"#{tc} {postorder_eval(1)}")