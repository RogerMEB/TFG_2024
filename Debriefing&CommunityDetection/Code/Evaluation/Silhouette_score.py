import networkx as nx
import numpy as np
from sklearn.metrics import silhouette_score
from community import community_louvain
import matplotlib.pyplot as plt

def create_similarity_graph(similarity_scores):
    G = nx.Graph()
    for (student1, student2), score in similarity_scores.items():
        G.add_edge(student1, student2, weight=score)
    return G

def apply_louvain_method(G):
    partition = community_louvain.best_partition(G, weight='weight')
    return partition

def compute_silhouette_score(G, partition):
    adj_matrix = nx.to_numpy_matrix(G, nodelist=G.nodes())
    labels = np.array([partition[node] for node in G.nodes()])
    silhouette_avg = silhouette_score(adj_matrix, labels, metric='precomputed')
    return silhouette_avg

def plot_graph(G, partition):
    pos = nx.spring_layout(G)
    colors = [partition[node] for node in G.nodes()]
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color=colors, cmap=plt.cm.rainbow, node_size=500, edge_color='gray')
    plt.title("Student Similarity Graph with Communities")
    plt.show()

# Example usage
"""similarity_scores = {
      ('A', 'B'): 0.8,
      ('A', 'C'): 0.6,
      ('A', 'D'): 0.2,
      ('B', 'C'): 0.7,
      ('B', 'D'): 0.3,
      ('C', 'D'): 0.4,
}

G = create_similarity_graph(similarity_scores)
partition = apply_louvain_method(G)
silhouette_avg = compute_silhouette_score(G, partition)
print(f"Silhouette Score: {silhouette_avg}")
plot_graph(G, partition)"""

