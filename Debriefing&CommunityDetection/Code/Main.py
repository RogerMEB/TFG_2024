import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Importing functions from other files
from Feature_extraction import z_normalize, array_similarity, direct_similarity, min_max_norm, overall_similarity
from Louvain import Louvain_classification, Plot_communities
from LPA import LPA_classification
from Circle_plot import display_circles
from Tables import display_low_high_similarity_students

def main():

    # Define the ratings matrix (example data)
    ratings_matrix = np.array([
        [5, 5, 5, 5],  # Ratings of student A
        [4, 4, 3, 3],  # Ratings of student B
        [4, 5, 5, 4],  # Ratings of student C
        [4, 5, 5, 4],  # Ratings of student D
        [3, 4, 3, 4]   # Ratings of student E
    ])
    
    # Z-normalize ratings
    ratings_matrix_norm = np.apply_along_axis(z_normalize, 1, ratings_matrix)
    
    # Compute array similarities between all pairs of students
    num_students = ratings_matrix_norm.shape[0]
    array_sim_matrix = np.zeros((num_students, num_students))
    
    for i in range(num_students):
        for j in range(num_students):
            if i != j:
                array_sim_matrix[i, j] = array_similarity(ratings_matrix_norm[i], ratings_matrix_norm[j])
    
    # Compute direct similarities
    direct_sim_matrix = np.zeros((num_students, num_students))
    
    for i in range(num_students):
        for j in range(num_students):
            if i != j:
                direct_sim_matrix[i, j] = direct_similarity(ratings_matrix_norm[i], ratings_matrix_norm[j])
    
    # Normalize direct similarities
    direct_sim_matrix_norm = np.apply_along_axis(min_max_norm, 1, direct_sim_matrix)
    
    # Compute overall similarities
    overall_sim_matrix = np.zeros((num_students, num_students))
    w1, w2 = 0.5, 0.5  # Weights for the overall similarity
    
    for i in range(num_students):
        for j in range(num_students):
            if i != j:
                overall_sim_matrix[i, j] = overall_similarity(array_sim_matrix[i, j], direct_sim_matrix_norm[i, j], w1, w2)
    
    # Print overall similarity matrix
    print("Overall Similarity Matrix:")
    print(overall_sim_matrix)
    
    # Create the graph with overall similarity values as edge weights
    G = nx.Graph()    
    students = ['A', 'B', 'C', 'D', 'E']
    G.add_nodes_from(students)
    
    for i in range(num_students):
        for j in range(num_students):
            if i != j:
                G.add_edge(students[i], students[j], weight=overall_sim_matrix[i, j])
    
    # Perform Louvain classification
    partition = Louvain_classification(G)
    # partition = LPA_classification(G) example for LPA
    
    # Plot the communities
    Plot_communities(partition, G)

    mean_rating = np.mean(mean_ratings)  # Mean of mean ratings
    mean_similarity = np.mean(overall_sim_matrix)
    
    # Display the circle plots
    display_circles(mean_rating, mean_similarity)

    # Get similarity scores for each student
    similarity_scores = {}
    for i, student in enumerate(students):
        for j, other_student in enumerate(students):
            if i != j:
                similarity_scores[(student, other_student)] = overall_sim_matrix[i, j]

    # Compute mean rating for each student
    mean_ratings = np.mean(ratings_matrix, axis=1)

    # Display the table of students with top and low similarity scores
    display_low_high_similarity_students(similarity_scores, mean_ratings)

if __name__ == "__main__":
    main()


