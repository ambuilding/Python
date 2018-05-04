import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u", "v"])

G.nodes()

G.add_edge(1,2)
G.add_edge("u", "v")
G.add_edges_from([(1,3), (1,4), (1,5), (1,6)])
G.add_edge("u", "w")

G.edges()
G.degree()

G.remove_node(2)
G.remove_nodes_from([4,5])

G.remove_edge(1,3)
G.remove_edges_from([(1, 6), ('u', 'v')])

G.number_of_nodes()
G.number_of_edges()

import matplotlib.pyplot as plt

G1 = nx.karate_club_graph()
nx.draw(G1, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")

G1.degree()

# We can use this dictionary to find the degree of a given node.
# Or alternatively, we can use to G dot degree function.
G1.degree(0) is G1.degree()[0]



