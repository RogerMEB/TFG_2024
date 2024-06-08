import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def Histogram(ratings):

    # Flatten ratings for histogram
    all_ratings = [rating for student_ratings in ratings.values() for rating in student_ratings]
    
    # Histogram of ratings
    plt.figure(figsize=(8, 6))
    plt.hist(all_ratings, bins=range(0, 7), align='left', edgecolor='black', alpha=0.7)
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title('Histogram of Ratings')
    plt.xticks(range(0, 6))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def Scatter_plot(ratings):
    
    # Scatter plot of ratings
    plt.figure(figsize=(8, 6))
    for student, student_ratings in ratings.items():
        plt.scatter([student] * len(student_ratings), student_ratings, label=student)
    
    plt.xlabel('Student')
    plt.ylabel('Rating')
    plt.title('Scatter Plot of Ratings')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def Box_plot(ratings):
    
    df = pd.DataFrame(ratings)
    
    # Create the boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df)
    
    # Set the title and labels
    plt.title('Boxplot of Ratings by Students')
    plt.xlabel('Students')
    plt.ylabel('Ratings')
    plt.show()

def Heatmap(ratings):

    # Convert the similarity scores to a DataFrame
    df = pd.DataFrame(ratings)
    
    # Create a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df, annot=True, cmap="YlGnBu", cbar=True, linewidths=.5)
    
    # Set the title and labels
    plt.title('Heatmap of Similarity Scores')
    plt.xlabel('Students')
    plt.ylabel('Students')
    
    # Show the plot
    plt.show()

""" Example usage 
# Ratings of the students (The same can be plotted if the similarity score is provided)
ratings = {
    'A': [1, 2, 1],
    'B': [5,4,4],
    'C': [3,3,2],
    'D': [5,5,5]
}

Histogram(ratings)
Scatter_plot(ratings)
Box_plot(ratings)
Heatmap(ratings)"""