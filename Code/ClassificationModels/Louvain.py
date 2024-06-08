import networkx as nx
import matplotlib.pyplot as plt

# Function to apply Louvain method for community detection
def Louvain_classification(G):
    return nx.community.greedy_modularity_communities(G)

# Function to plot communities
def Plot_communities(partition, G):
    # Create a color map for communities
    community_map = {}
    for idx, community_nodes in enumerate(partition):
        for node in community_nodes:
            community_map[node] = idx
    
    # Draw the graph with nodes colored by community
    pos = nx.spring_layout(G)
    node_colors = [community_map[node] for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.tab10, node_size=1000, font_size=15, font_weight='bold')
    
    plt.title('Student Similarity Graph with Communities (Louvain Method)')
    plt.show()

""" Example data
students = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B', {'weight': 0.55}), ('A', 'C', {'weight': 0.785}), ('A', 'D', {'weight': 0.735}), ('A', 'E', {'weight': 0.55}),
         ('B', 'C', {'weight': 0.7}), ('B', 'D', {'weight': 0.6}), ('B', 'E', {'weight': 0.685}),
         ('C', 'D', {'weight': 0.95}), ('C', 'E', {'weight': 0.65}), ('D', 'E', {'weight': 0.6})]

# Create the graph
G = nx.Graph()    
G.add_nodes_from(students)
G.add_edges_from(edges)

# Perform Louvain classification
partition = Louvain_classification(G)

# Plot the communities
Plot_communities(partition, G)"""
