import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

def Create_similarity_matrix(group):
    """
    Creates a similarity matrix from the group's similarity data.
    """
    students = group['students']
    student_indices = {student: idx for idx, student in enumerate(students)}
    n = len(students)
    
    # Initialize similarity matrix with zeros
    similarity_matrix = np.zeros((n, n))
    
    for edge in group['similarity']:
        student1, student2, attr = edge
        idx1 = student_indices[student1]
        idx2 = student_indices[student2]
        similarity_matrix[idx1][idx2] = attr['weight']
        similarity_matrix[idx2][idx1] = attr['weight']
    
    return similarity_matrix, students

def KMeans_classification(group, n_clusters=2):
    """
    Applies KMeans clustering to the similarity matrix and returns the cluster labels.
    """
    similarity_matrix, students = Create_similarity_matrix(group)
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(similarity_matrix)
    labels = kmeans.labels_
    
    # Create partition dictionary
    partition = {students[i]: labels[i] for i in range(len(students))}
    
    return partition

def Plot_KMeans_clusters(G, partition):
    """
    Plots the graph with nodes colored based on KMeans cluster labels.
    """
    # Create a color map for clusters
    cluster_map = partition
    
    # Draw the graph with nodes colored by cluster
    pos = nx.spring_layout(G)
    node_colors = [cluster_map[node] for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.tab10, node_size=1000, font_size=15, font_weight='bold')
    
    # Add edge labels (similarity scores)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=12)
    
    plt.title('Similarity Graph with KMeans Clusters')
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

# Create the graph
G = nx.Graph()
G.add_nodes_from(group['students'])
G.add_edges_from(group['similarity'])

# Apply KMeans classification
partition = KMeans_classification(group, n_clusters=2)
Plot_KMeans_clusters(G, partition)"""
