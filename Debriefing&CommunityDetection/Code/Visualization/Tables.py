import pandas as pd
import numpy as np

# Function to color cells based on their values
def color_by_value(value):
    if value <= 1:
        if value >= 0.8:
            return 'background-color: blue; color: white'
        elif value >= 0.6:
            return 'background-color: green; color: black'
        elif value >= 0.4:
            return 'background-color: orange; color: black'
        else:
            return 'background-color: red; color: white'
    else:
        if value/5 >= 0.8:
            return 'background-color: blue; color: white'
        elif value/5 >= 0.6:
            return 'background-color: green; color: black'
        elif value/5 >= 0.4:
            return 'background-color: orange; color: black'
        else:
            return 'background-color: red; color: white'

def display_low_high_similarity_groups(similarity_scores, group_ratings):
    # Sort the groups based on similarity scores
    sorted_groups = sorted(similarity_scores.items(), key=lambda x: x[1])
    
    # Get the three lowest similarity score groups/students
    lowest_groups = sorted_groups[:3]
    
    # Get the three highest similarity score groups/students
    highest_groups = sorted_groups[-3:]
    
    # Create DataFrame for lowest similarity score groups
    lowest_df = pd.DataFrame(lowest_groups, columns=["Group", "Similarity Score"])
    lowest_df["Rating"] = [group_ratings[group] for group, _ in lowest_groups]
    lowest_df["Similarity Score"] = lowest_df["Similarity Score"].apply(lambda x: round(x, 2))
    
    # Create DataFrame for highest similarity score groups
    highest_df = pd.DataFrame(highest_groups, columns=["Group", "Similarity Score"])
    highest_df["Rating"] = [group_ratings[group] for group, _ in highest_groups]
    highest_df["Similarity Score"] = highest_df["Similarity Score"].apply(lambda x: round(x, 2))
    
    # Function to apply coloring
    def apply_coloring(df):
        return df.style.applymap(color_by_value, subset=['Similarity Score', 'Rating'])
    
    # Display DataFrames with titles
    display(apply_coloring(lowest_df).set_caption("Most Conflictive Groups"))

    display(apply_coloring(highest_df).set_caption("Most Agreeing Groups"))

""" # Example usage
similarity_scores = {"Group 1": 0.45, "Group 2": 0.62, "Group 3": 0.28, "Group 4": 0.75, "Group 5": 0.83}
group_ratings = {"Group 1": 4.5, "Group 2": 3.8, "Group 3": 4.2, "Group 4": 4.9, "Group 5": 4.6}

display_low_high_similarity_groups(similarity_scores, group_ratings)"""