import sys
sys.stdin = open("input.txt", "r")

T = 10 # number of test case
for cs in range(1, T+1):

    roots_count = int(input())
    tree_base = [0] * (roots_count+1) # make tree base has length as much as root_count

    for i in range(roots_count):
        input_data = list(input().split())
        # first input data value mean index
        idx = int(input_data[0])
        # second
        value = input_data[1]
        tree_base[idx] = value


    result = []  # result list

    def inorder_traversal(idx):
        if idx <= roots_count and tree_base[idx] != 0:
            inorder_traversal(idx * 2)
            result.append(tree_base[idx])
            inorder_traversal(idx * 2 + 1)

    inorder_traversal(1)  # start from 1 cause index of root node is 1
    print(f"#{cs} {''.join(result)}")
