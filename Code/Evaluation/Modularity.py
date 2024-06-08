import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def Compute_modularity(G, partition):
    modularity_value = nx.community.modularity(G, partition)
    return modularity_value

def Modularity_matrix(G):
    # Compute modularity matrix
    mod_matrix = nx.modularity_matrix(G, nodelist=G.nodes())
    
    # Plot modularity matrix
    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.matshow(mod_matrix, cmap=plt.cm.Blues)
    fig.colorbar(cax)
    
    ax.set_xticks(range(len(G.nodes())))
    ax.set_yticks(range(len(G.nodes())))
    ax.set_xticklabels(G.nodes())
    ax.set_yticklabels(G.nodes())
    
    plt.title('Modularity Matrix')
    plt.show()

def Plot_modularity_vs_community_count(G):
    from networkx.algorithms.community import greedy_modularity_communities
    import itertools
    
    # Find communities using Greedy Modularity method
    communities = greedy_modularity_communities(G)
    
    # Compute modularity for different numbers of communities
    modularity_values = []
    for k in range(1, len(communities)+1):
        k_communities = list(itertools.islice(communities, k))
        modularity_values.append(nx.community.modularity(G, k_communities))
    
    # Plot modularity values
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(range(1, len(communities)+1), modularity_values, marker='o')
    ax.set_xlabel('Number of Communities')
    ax.set_ylabel('Modularity')
    ax.set_title('Modularity vs Number of Communities')
    
    plt.show()

# Example usage

""" G = nx.Graph()

# Add nodes with student labels
# students = ['A', 'B', 'C', 'D', 'E']
# G.add_nodes_from(students)

# Add edges with similarity scores
# edges = [('A', 'B', {'weight': 0.55}), ('A', 'C', {'weight': 0.785}), ('A', 'D', {'weight': 0.735}), ('A', 'E', {'weight': 0.55}),
#          ('B', 'C', {'weight': 0.7}), ('B', 'D', {'weight': 0.6}), ('B', 'E', {'weight': 0.685}),
#          ('C', 'D', {'weight': 0.95}), ('C', 'E', {'weight': 0.65}), ('D', 'E', {'weight': 0.6})]

# G.add_edges_from(edges)

# Apply Louvain (for example) method for community detection
# partition = nx.community.louvain_communities(G)

# Compute modularity
# modularity_value = Compute_modularity(G, partition)
# print("Modularity Value:", modularity_value)

# Plot modularity matrix
# Modularity_matrix(G)

# Plot modularity vs number of communities
# Plot_modularity_vs_community_count(G)"""


