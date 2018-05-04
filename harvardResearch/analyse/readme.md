## Social Network Analysis

### Network analysis can be used to
- study how pathogens, behaviors, and information spread in social networks,
- having important implications for our understanding of epidemics
- and the planning of effective interventions.
- In a biological context, at a molecular level,
  - network analysis can be applied to gene regulation networks,
  - signal transduction networks,
  - protein interaction networks, and much, much more.

- Some basic concepts about networks
- Write a Python function Generate very simple random graphs
- Finally, analyze some basic properties of social networks collected in different rural villages in India.

### About
- the basic components of networks and the graphs that represent them
  - such as neighbor, degree, path, component, and largest connected component.
  - Network refers to the real world object, such as a road network,
  - whereas a graph refers to its abstract mathematical representation.
  - Any component is connected when considered on its own,
  - but there are no edges between the nodes that belong to different components.

##### Basic network concepts
- Graphs consist of `nodes`, also called `vertices`, and `links`, also called `edges`.
- Mathematically, a graph is a collection of vertices and edges where each edge corresponds to a pair of vertices.
- When we visualize graphs, we typically draw vertices as circles and
  - edges as lines connecting the circles.
- The `degree` of a vertex is the number of entries connected to it
- A `path` is a sequence of unique vertices,
  - such that any two vertices in the sequence are connected by an edge.
- The length of a path is defined as the number of edges in that path.
- if there is a path from every vertex to every other vertex, connected.
- If a graph is not connected, disconnected.
- If a graph is disconnected, it breaks apart naturally into pieces, or components.
  - Any component is connected when considered on its own,
  - but there are no edges between the nodes that belong to different components.
- the largest connected component, the one having the greatest number of nodes.

#####  Basics of NetworkX
- use the NetworkX module to create and manipulate network graphs
  - visualize a graph
  - `G.degree()` Networkx stores the degrees of nodes in a dictionary where
  - the keys are node IDs and the values are their associated degrees.

- write a Python function to generate very simple random graphs,
  - Erdős-Rényi (ER), Two paramenters
  - capital `N` is the number of nodes in the graph,
  - lowercase `p` is the probability for any pair of nodes to be connected by an edge.
  - writing our own ER function to better understand the model.
  - how to implement the coin flip just one time.
    - Use the SciPy stats module, more specifically a function called Bernoulli.
    - The only input argument is p, which is the probability of success.
    - That means that p is the probability that we get an outcome 1 as opposed to outcome 0.
    - Because our graph is undirected, we should consider each pair of nodes just one time.

- plot the degree distribution of a graph
  - P of k, the probability of observing a node with that degree.
  - The majority of the nodes appear to have somewhere between perhaps 35 and 50 connections.

#### Descriptive Statistics of Empirical Social Networks
- Look at the basic properties of social networks in two villages in rural India
- Compare the degree distribution of these empirical networks with the degree distribution of the ER networks

##### Adjacency matrix
- The structure of connections in a network can be captured in what is known as the Adjacency matrix of the network.
- If we have n nodes, this is n by n matrix, where entry ij is one if node i and node j have a tie between them.(undirected)
- Otherwise, that entry is equal to zero.

- Consequently, the adjacency matrix is symmetric.
- That means that the element ij is always the same as the element ji.
- Either both are zero or both are equal to 1.

- convert the adjacency matrices to graph objects.
- To get a basic sense of the network size and number of connections,
  - count the number of nodes and the number of edges in the networks.
  - Each node has a total number of edges, its degree.
  - Calculate the mean degree for all nodes in the network.


- [Banerjee et al. 2013: The Diffusion of Microfinance](http://science.sciencemag.org/content/341/6144/1236498.full)
- These data are part of a much larger dataset that was collected
to study diffusion of micro-finance.


```
It seems that most people have relatively few connections,
whereas a small fraction of people have a large number of connections.
This distribution doesn't look at all symmetric,
and its tail extends quite far to the right.
This suggests that the ER graphs are likely not good models
for real world social networks
```

#### find/visualize the largest connected component in a network
- extract all components for graph `nx.connected_component_subgraphs()`
  - Generator functions do not return a single object,
  - can be used to generate a sequence of objects using the next method.
- In practice, it is very common for networks to contain one component that
  - encompasses a large majority of its nodes, 95, 99, or even 99.9% of all of the nodes.

- groups are called network communities.
  - And the idea is that a community is a group of nodes that
  - are densely connected to other nodes in the group,
  - but only sparsely connected nodes outside of that group.
  - Finding network communities is a very interesting and timely problem.


### Network homophily
- It occurs when nodes that share an edge share a characteristic
  - more often than nodes that do not share an edge.

#### Investigate homophily of several characteristics of individuals connected in social networks in rural India.
- calculate the chance homophily for an arbitrary characteristic.
  - dict / characteristics : the frequency of their occurrence
  - the frequency of a squared and sum
- Homophily is the proportion of edges in the network whose constituent nodes share that characteristic.

- calculate and compare the actual homophily in these village to chance.
- subset the data into individual villages and store them.
- define a few dictionaries that enable us to look up
  - the sex, caste, and religion of members of each village by personal ID.
- create a function that computes the observed homophily given a village and characteristic.
