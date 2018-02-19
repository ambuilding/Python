import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")

G.degree()

# G.degree(0) is G.degree()[0]

from scipy.stats import bernoulli

#bernoulli.rvs(p=0.2)

# create empty graph
# add all N nodes in the graph
# loop over all pairs of nodes
    # add an edge with prob p
def er_graph(N, p):
    """Generate an ER graph."""
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
    plt.hist(list(G.degree().values()), histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("%P(k)$")
    plt.title("Degree distribution")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    