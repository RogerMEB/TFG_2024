import matplotlib.pyplot as plt
import numpy as np

def color_by_value_bar(value):
    if value >= 0.8:
        return 'blue'
    elif value >= 0.6:
        return 'green'
    elif value >= 0.4:
        return 'orange'
    else:
        return 'red'

def plot_similarity_bar_chart(similarity_scores):
    groups = list(similarity_scores.keys())
    scores = list(similarity_scores.values())
    colors = [color_by_value_bar(score) for score in scores]
    
    fig, ax = plt.subplots()
    bars = ax.bar(groups, scores, color=colors)
    
    # Add labels and title
    ax.set_ylabel('Convergence level')
    ax.set_xlabel('Groups')
    ax.set_title('Agreement of all Groups')
    ax.set_ylim(0, 1)  # Set y-axis range from 0 to 1

    # Adding color legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='green', edgecolor='black', label='>= 0.8'),
                       Patch(facecolor='yellow', edgecolor='black', label='0.6 - 0.79'),
                       Patch(facecolor='orange', edgecolor='black', label='0.4 - 0.59'),
                       Patch(facecolor='red', edgecolor='black', label='< 0.4')]
    #ax.legend(handles=legend_elements, title='Similarity Score')

    # Add text annotations for the similarity scores
    #for bar, score in zip(bars, scores):
        #ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.05, f'{score:.2f}', ha='center', color='black')

    plt.show()

"""# Example usage
similarity_scores = {"1": 0.45, "2": 0.62, "3": 0.28, "4": 0.75, "5": 0.83, "6":0.25, "7":0.43,
                    "8":0.92, "9": 0.65, "10": 0.33, "11":0.77, "12": 0.72, "13": 0.88}
plot_similarity_bar_chart(similarity_scores)"""
