import networkx as nx
import matplotlib.pyplot as plt

# Example data: Similarity scores between students in a group
similarity_scores = {
    ('A', 'B'): 0.75, ('A', 'C'): 0.60, ('A', 'D'): 0.45, ('A','E'):0.21,
    ('B', 'C'): 0.85, ('B', 'D'): 0.55, ('B','E'):0.76,
    ('C', 'D'): 0.70, ('C','E'):0.92, ('D','E'):0.41
}

# Create the graph
G = nx.Graph()

# Add nodes
students = set()
for pair in similarity_scores.keys():
    students.update(pair)
G.add_nodes_from(students)

# Add edges with similarity scores as weights
for (u, v), weight in similarity_scores.items():
    G.add_edge(u, v, weight=weight)

# Function to color edges based on similarity score
def color_by_value(value):
    if value >= 0.8:
        return 'blue'
    elif value >= 0.6:
        return 'green'
    elif value >= 0.4:
        return 'orange'
    else:
        return 'red'

# Calculate mean similarity score for each node
mean_scores = {student: 0 for student in students}
count = {student: 0 for student in students}

for (u, v), weight in similarity_scores.items():
    mean_scores[u] += weight
    mean_scores[v] += weight
    count[u] += 1
    count[v] += 1

mean_scores = {student: mean_scores[student] / count[student] for student in students}

# Function to color nodes based on mean similarity score
def node_color_by_mean_score(value):
    if value >= 0.8:
        return 'blue'
    elif value >= 0.6:
        return 'green'
    elif value >= 0.4:
        return 'orange'
    else:
        return 'red'

# Get colors for edges and nodes
edge_colors = [color_by_value(G[u][v]['weight']) for u, v in G.edges()]
node_colors = [node_color_by_mean_score(mean_scores[node]) for node in G.nodes()]

# Draw the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))

# Draw nodes with colors
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500, cmap=plt.cm.RdYlGn)

# Draw edges with colors
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

# Create legend for edge colors
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='blue', edgecolor='black', label='>= 0.8'),
                   Patch(facecolor='green', edgecolor='black', label='0.6 - 0.79'),
                   Patch(facecolor='orange', edgecolor='black', label='0.4 - 0.59'),
                   Patch(facecolor='red', edgecolor='black', label='< 0.4')]

plt.legend(handles=legend_elements, title='Agreement')
plt.title('Student agreement network Group 5')
plt.show()

