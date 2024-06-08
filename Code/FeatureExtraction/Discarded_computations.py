import numpy as np
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import pandas as pd

# Discarded computations

def z_normalization(ratings):
    """
    Perform Z-normalization on the ratings.
    """
    return (ratings - ratings.mean()) / ratings.std()

def array_similarity(arr1, arr2):
    """
    Compute the similarity between two arrays using different metrics.
    """
    # Cosine similarity
    cos_sim = cosine_similarity([arr1], [arr2])[0][0]
    
    # Jaccard similarity (binary case)
    jaccard_sim = jaccard_score(arr1, arr2, average='binary')
    
    # Euclidean distance (convert to similarity)
    euclidean_dist = euclidean_distances([arr1], [arr2])[0][0]
    euclidean_sim = 1 / (1 + euclidean_dist)  # Normalize to (0, 1)
    
    return cos_sim, jaccard_sim, euclidean_sim

def direct_similarity(student1_ratings, student2_ratings):
    """
    Compute direct similarities between ratings of two students.
    """
    return array_similarity(student1_ratings, student2_ratings)

def normalize_similarity(similarities):
    """
    Normalize similarities to a (0, 1) range.
    """
    similarities = np.array(similarities)
    return (similarities - similarities.min()) / (similarities.max() - similarities.min())

def overall_similarity(students_ratings):
    """
    Compute the overall similarity matrix for a group of students.
    """
    n = len(students_ratings)
    similarity_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i + 1, n):
            student1_ratings = students_ratings[i]
            student2_ratings = students_ratings[j]
            cos_sim, jaccard_sim, euclidean_sim = direct_similarity(student1_ratings, student2_ratings)
            overall_sim = (cos_sim + jaccard_sim + euclidean_sim) / 3
            similarity_matrix[i][j] = similarity_matrix[j][i] = overall_sim
    
    return similarity_matrix

def feature_extraction(students_ratings):
    """
    Extract features for all pairwise comparisons between students.
    """
    similarity_matrix = overall_similarity(students_ratings)
    return similarity_matrix

"""# Example usage
# Example data
students_ratings = np.array([
     [1, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 1, 1],
     [0, 0, 1, 1],
     [1, 0, 0, 1]
])

# Compute similarity matrix
similarity_matrix = feature_extraction(students_ratings)
print(similarity_matrix)"""
