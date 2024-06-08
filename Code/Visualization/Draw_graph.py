import networkx as nx
import matplotlib.pyplot as plt

def Draw_graph(group):
    """
    Draws a similarity graph for the given group.
    """
    # Create the graph
    G = nx.Graph()
    
    # Add nodes with the student labels
    students = group['students']
    G.add_nodes_from(students)
    
    # Add edges with similarity scores
    edges = group['similarity']
    G.add_edges_from(edges)
    
    # Draw the graph
    pos = nx.spring_layout(G)  # Positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=15, font_weight='bold')
    
    # Add edge labels (similarity scores)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=12)
    
    plt.title('Similarity Graph Group ' + str(group['id']))
    plt.show()

def Colorize_graph_partition(G, partition):
    """
    Draws the graph with nodes colored by their partition.
    """
    # Create a color map for communities
    community_map = {}
    for idx, community_nodes in enumerate(partition):
        for node in community_nodes:
            community_map[node] = idx
    
    # Draw the graph with nodes colored by community
    pos = nx.spring_layout(G)
    node_colors = [community_map[node] for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.tab10, node_size=1000, font_size=15, font_weight='bold')
    
    # Add edge labels (similarity scores)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=12)
    
    plt.title('Similarity Graph with Communities')
    plt.show()

""" Example usage
# Example group
group = {
     'students': ['A', 'B', 'C', 'D', 'E'],
     'similarity': [('A', 'B', {'weight': 0.55}), ('A', 'C', {'weight': 0.785}), ('A', 'D', {'weight': 0.735}), ('A', 'E', {'weight': 0.55}),
                    ('B', 'C', {'weight': 0.7}), ('B', 'D', {'weight': 0.6}), ('B', 'E', {'weight': 0.685}),
                    ('C', 'D', {'weight': 0.95}), ('C', 'E', {'weight': 0.65}), ('D', 'E', {'weight': 0.6})],
     'id': 0
}

Draw_graph(group)

#Example partition data for colorizing
partition = [['A', 'C', 'D'], ['B', 'E']]

# Create the graph
G = nx.Graph()
G.add_nodes_from(group['students'])
G.add_edges_from(group['similarity'])

# Colorize_graph_partition(G, partition)
d':0})"""