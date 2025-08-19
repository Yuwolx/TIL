# Disjoint set

**There is no common atom in each set**

## How to representation mutial beta set
- connected list
- tree

### Tree
make list by tuple type like (1,b)
- it's mean b has index about location and present parent of b is 1
- in short, (parent_index, itself)

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

### Union with Rank
- each node store root's subtree height as rank
- use two list, parent and rank
- define function in python have to return one result
  - so result should be link tuple, each value