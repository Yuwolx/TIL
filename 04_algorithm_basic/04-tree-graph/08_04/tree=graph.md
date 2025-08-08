## tree-graph
**hierarchical  data structure**

### Tree
- **Have 1:N relation with atoms(children)**
    - unliner: so seems like tree(back-side slip)
    
- Root
    - The first node (in relation structure)
    - leaf node: the last nodes
- edge
  - link between nodes
- degree
  - The number of children each node
- Level
  - Distinct to other node in vertical
  - root node's level is 0 
- Height of tree : distance in root to leaf : number of edge 

#### Binary Tree
**Each node have maximum two children node**
  - Call left child node/right child node
- If every node has two children node
  - **Perfect binary tree**
  
- **Complete Binary tree**
  - All node number filled continually
  
- **Skewed Binary tree**
  - Every node has one side. child node 
  
#### How to representation Binary tree
**use list with index**

### explore tree
**traversal**
visit every node specific order
- "visit"'s mean is standard in process order 

- Tree way of traversal
  - Preorder_traversal: VLR
    - procedure: VLLLRRR (not vlrvlrvlr)
    - Cause Left child node is root in sub tree
    
  - Inorder_traversal: LVR
    - The most left leaf node start on traversal to parent side 
    
  - Postorder_traversal: LRV
  
### How to make tree as list
Depend on data shape

### Expression Tree
Consist number and string(operators)

## Graph
**In graph each node has N:M relation with other nodes**
- Vertex
  - dot
- Edge
  - line
- Degree
 - number of line each node

**Graph has several kinds**
There is direction
  - If have direciton, divided in and out
  - Should be check cycle's presence

Which dots connected by enge, then can call adjacency