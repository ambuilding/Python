import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

bernoulli.rvs(p=0.5)

flip_coin_1000_times = sum([bernoulli.rvs(p=0.5) for t in range(1000)])

# create empty graph
# add all N nodes in the graph
# loop over all pairs of nodes
    # add an edge with prob p
def er_graph(N, p):
    """
    Generate an ER graph.
    capital `N` is the number of nodes in the graph,
    lowercase `p` is the probability for 
    any pair of nodes to be connected by an edge.
    """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G
            
nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")

def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    #  P of k, the probability of observing a node with that degree.
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")
    
G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist3.pdf")
    
    
import numpy as np

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",") 

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)
    
def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    #np.mean(list(dict(G1.degree()).values()))
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))

basic_net_stats(G1)
basic_net_stats(G2)
    
plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")
    

#gen = nx.connected_component_subgraphs(G1)
#g = gen.__next__()
#g = gen.__next__()
#len(gen.__next__())
G1_LCC = max(nx.connected_component_subgraphs(G1), key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key=len)
G1_LCC.number_of_nodes() / G1.number_of_nodes()
G2_LCC.number_of_nodes() / G2.number_of_nodes()

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")
    

    
    
    