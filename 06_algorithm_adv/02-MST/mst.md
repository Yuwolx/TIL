# Minimum Spanning Tree (MST)

## Definition

A **Minimum Spanning Tree (MST)** is a subgraph of a connected, undirected, weighted graph that:

* **Spans all vertices** (includes every vertex of the original graph),
* **Forms a tree** (no cycles, fully connected),
* Has the **minimum possible total edge weight** among all spanning trees.


## Key Properties

* For a graph with **V vertices**, an MST always contains **V - 1 edges**.
* An MST is **not unique** if there are multiple edges with equal weights that can replace each other.
* The graph must be **connected**; otherwise, a spanning tree (and thus MST) does not exist.
* Removing or adding any edge in an MST either:

  * Disconnects the graph, or
  * Creates a cycle (breaking the definition of a tree).


## Intuition

* A spanning tree is essentially a **subset of edges** that connects all vertices without cycles.
* To make it “minimum,” we **select edges with the smallest weights** while maintaining connectivity and avoiding cycles.
* Think of it as **connecting cities with roads at the lowest possible cost**.


## Applications

* **Network design** (e.g., laying out cables, roads, pipelines with minimum cost).
* **Approximation algorithms** (e.g., Traveling Salesman Problem).
* **Clustering** (e.g., hierarchical clustering using MST-based methods).
* **Image processing** (e.g., segmentation).


## Famous Algorithms

1. **Kruskal’s Algorithm**

   * Sort all edges by weight.
   * Add the smallest edge to the MST if it doesn’t form a cycle (using Disjoint Set Union to check).
   * Repeat until MST has `V - 1` edges.

2. **Prim’s Algorithm**

   * Start from any vertex.
   * Grow the tree by repeatedly adding the smallest edge that connects the tree to a new vertex.

3. **Borůvka’s Algorithm** (less common but foundational).


✅ In short:

> MST = “A tree that connects all vertices with the least total edge weight, without cycles.”

