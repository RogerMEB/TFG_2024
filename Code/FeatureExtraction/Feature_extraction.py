import numpy as np
from scipy.stats import zscore

def z_normalize(ratings):
    """
    Z-normalizes the ratings.
    
    Parameters:
    ratings (list or array): Ratings to normalize.
    
    Returns:
    array: Z-normalized ratings.
    """
    return zscore(ratings)

def array_similarity(ratingsA, ratingsB):
    """
    Computes the similarity between two arrays of ratings using the absolute difference.
    
    Parameters:
    ratingsA (list or array): Ratings of student A.
    ratingsB (list or array): Ratings of student B.
    
    Returns:
    float: Similarity score between the two arrays.
    """
    return 1 - np.mean(np.abs(ratings1 - ratings2))

def direct_similarity(rating_a_to_b, rating_b_to_a):
    """
    Computes the direct similarity between two students.
    
    Parameters:
    rating_a_to_b (float): Rating of student A to student B.
    rating_b_to_a (float): Rating of student B to student A.
    
    Returns:
    float: Direct similarity score between the two students.
    """
    return (rating_a_to_b + rating_b_to_a) / 2

def min_max_norm(score, min_value=0, max_value=5):
    """
    Normalizes a similarity score to a range between 0 and 1.
    
    Parameters:
    score (float): The similarity score to normalize.
    min_value (float): The minimum possible value of the score.
    max_value (float): The maximum possible value of the score.
    
    Returns:
    float: Normalized similarity score.
    """
    return (score - min_value) / (max_value - min_value)

def overall_similarity(array_sim, direct_sim,w1,w2):
    """
    Computes the overall similarity score as the weighted sum of the previous features.
    
    Parameters:
    array_sim (float): Array similarity score.
    direct_sim (float): Direct similarity score.
    w1: weight of array_sim in the overall score
    w2: weight of the direct_sim in the overall score
    
    Returns:
    float: Overall similarity score.
    """
    return w1*array_sim + w2*direct_sim 

# Example usage:
"""ratings_A = [5, 5, 5, 5]
ratings_B = [4, 4, 3, 3]
ratings_C = [4, 5, 5, 4]
ratings_D = [4, 5, 5, 4]
ratings_E = [3, 4, 3, 4]

# Z-normalize ratings
ratings_A_norm = z_normalize(ratings_A)
ratings_B_norm = z_normalize(ratings_B)
ratings_C_norm = z_normalize(ratings_C)
ratings_D_norm = z_normalize(ratings_D)
ratings_E_norm = z_normalize(ratings_E)

# Compute array similarities
sim_A_B = array_similarity(ratings_A_norm, ratings_B_norm)
sim_A_C = array_similarity(ratings_A_norm, ratings_C_norm)
sim_A_D = array_similarity(ratings_A_norm, ratings_D_norm)
sim_A_E = array_similarity(ratings_A_norm, ratings_E_norm)

# Direct similarity (example ratings)
rating_A_to_B = 3
rating_B_to_A = 4
direct_sim_A_B = direct_similarity(rating_A_to_B, rating_B_to_A)

# Normalize direct similarity
normalized_direct_sim_A_B = min_max_norm(direct_sim_A_B)

# Compute overall similarity
overall_sim_A_B = overall_similarity(sim_A_B, normalized_direct_sim_A_B,0.5,0.5)

print(f"Overall similarity between A and B: {overall_sim_A_B}")"""
