# Disjoint set

**There is no common atom in each set**

## How to representation mutial beta set
- connected list
- tree

### Tree
**can indicate int list**
each index mean itself
each value mean index's parent

- can corporate with other root (= Union)
  -  then, one root stay root the other goes to node has new representative(parent)

- parent[i] = j
  - It' mean parent of i is j

## Developing mode in disjoint set

### Path compression
- every node connect directly to root 
```
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
```

### Union with Rank
- each node store root's subtree height as rank
- use two list, parent and rank
- define function in python have to return one result
  - so result should be link tuple, each value

```
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

```