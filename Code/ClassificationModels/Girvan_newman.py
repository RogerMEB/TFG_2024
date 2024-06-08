import networkx as nx
from networkx.algorithms.community import girvan_newman
import matplotlib.pyplot as plt

def Girvan_Newman_classification(G):
    communities = girvan_newman(G)
    return next(communities)

def Plot_communities(G, communities):
    # Create a color map for each community
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx

    # Get a list of colors for each node
    node_colors = [color_map[node] for node in G.nodes()]
    
    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, node_color=node_colors, with_labels=True, cmap=plt.cm.rainbow, node_size=500, font_size=16)
    plt.title('Girvan-Newman Community Detection')
    plt.show()

""" Example usage:
G = nx.Graph()

# Add nodes and edges (example graph)
edges = [
    ('A', 'B', 0.55), ('A', 'C', 0.90), ('A', 'D', 0.90), ('A', 'E', 0.70),
    ('B', 'C', 0.50), ('B', 'D', 0.65), ('B', 'E', 0.55),
    ('C', 'D', 0.75), ('C', 'E', 0.90),
    ('D', 'E', 0.75)
]

G.add_weighted_edges_from(edges)

# Apply Girvan-Newman algorithm
communities = Girvan_Newman_classification(G)

# Plot the graph with communities
Plot_communities(G, communities)"""
