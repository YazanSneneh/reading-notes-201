# Graphs
- A graph is a data structure that a collection of vertices potentially connected by line segments named edges.

### common terminology
- **Vertex** - a data object that can have zero or more adjacent vertices.
- **Edge** - An edge is a connection between two nodes.
- **Neighbor** - The neighbors of a node are its adjacent nodes are connected via an edge.
- **Degree** - The degree of a vertex is the number of edges connected to that vertex.

### Directed vs Undirected
##### Undirected Graphs
- each edge is undirected or bi-directional, meaning undirected graph does not move in any direction.
    - There are no “directions” given to point to specific vertices.
    - **Example**:
    ![undirected graph](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-35/resources/assets/UndirectedGraph.PNG)
    - **Vertices/Nodes** = {a,b,c,d,e,f}
    - **Edges** = {(a,c),(a,d),(b,c),(b,f),(c,e),(d,e),(e,f)}

##### Directed Graphs
- a graph where every edge is directed.
- Each node is directed at another node.
- **Example**: 
  ![directed graph](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-35/resources/assets/DirectedGraph.PNG)
    - **Vertices** = {a,b,c,d,e,f}
    - **Edges** = {(a,c),(b,c),(b,f),(c,e),(d,a),(d,e)(e,c)(e,f)}

### Complete vs Connected vs Disconnected
- types of graphs depends on how connected the graphs are to other node/vertices.
##### Complete Graphs
 - complete graph is when all nodes are connected to all other nodes.

##### Connected
- connected graph is graph that has all of vertices/nodes have at least one edge.
##### Disconnected
- disconnected graph is a graph where some vertices may not have edges.

### Acyclic vs Cyclic

#### Acyclic Graph
- Acyclic graph is a **directed** graph **without cycles**.
- node can be traversed through and potentially end up back at itself.
- directed acyclic graph is also called a **DAG**. This can also be represented as a **tree**.


#### Cyclic Graph
- cycle is a path starts and ends at the same vertex.

### Graph Representation
- represented graphs can be through Adjacency Matrix and Adjacency List.

#### Adjacency Matrix
- Adjacency matrix is represented through a 2-dimensional array. If there are n vertices, then we are looking at an n x n Boolean matrix


#### Adjacency List