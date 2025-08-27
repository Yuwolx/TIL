

v, e = map(int, input().split())

edges = []
for _ in range(e):
    a,b,rate = map(int, input().split())

    edges.append([rate, a,b])
    
edges.sort()

parent = [i for i in range(e+1)]
    # print(f'v,e: {v,e}')
    # print(f'edges[rate,a,b]: {edges}')
    # print(f'parent: {parent}')

# find parent of nodes
def mammamia(x):
    # if x has mother
    if parent[x] != x:
        # check grandmother
        parent[x] = parent[parent[x]]
        x = parent[x]
    # There is no x's mother
    # or After find root
    return x

# merge each set that have two node
def merge(a, b):
    # find root
    root_a, root_b = mammamia(a), mammamia(b)
    # if two root are different
    if root_a != root_b:
        # b tree attatch to a tree
        parent[root_b] = root_a
        # do merge
        return True
    # do not merge
    return False

# run Krusval
mst, cnt = 0, 0
for rate,a,b in edges:
    # if do merge
    if merge(a, b):
        mst += rate
        cnt += 1
        # need n-1 edges
        if cnt == v-1:
            break

print(mst)