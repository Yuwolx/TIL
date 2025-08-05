#DFS: Depth First Search
DFS is used to search in non-linear structures.

There’s no built-in "next" node, so you need a clear exploration strategy.

DFS explores deep first, then backtracks — great for pathfinding, puzzles, and more.ay

If in graph there are no root

So when searching in graph, have to need list saved visitied node

When definition function for DFS in graph
- At first, need vertex mean current visiting node
    -   vertex is index so, type of vertex is int
    
- Second, Find candidates connected
    - if there are candidates, use definited function start from new nodes in candidates
    - But didn't checking visitied node before, then occur infinity loof in function