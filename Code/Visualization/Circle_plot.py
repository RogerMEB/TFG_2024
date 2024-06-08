import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge, Circle, Patch

def plot_circle(ax, value, max_value=1.0, radius=1.0):
    # Determine color based on the value
    if value / max_value >= 0.8:
        color = 'blue'
    elif 0.6<= value/max_value < 0.8:
        color = 'green'
    elif 0.3 <= value/max_value < 0.6:
        color = 'orange'
    else:
        color = 'red'
    
    # Calculate the fraction of the circle to be filled
    theta = 2 * np.pi * value / max_value
    
    # Draw the background circle
    background_circle = Circle((0, 0), radius, color='lightgrey', alpha=0.5)
    ax.add_artist(background_circle)
    
    # Draw the filled portion of the circle
    filled_circle = Wedge((0, 0), radius, 0, np.degrees(theta), color=color)
    ax.add_artist(filled_circle)
    
    # Draw the inner circle over the main circle
    inner_circle = Circle((0, 0), radius * 0.5, color='white', alpha=1)
    ax.add_artist(inner_circle)
    
    # Add a text label with the value
    ax.text(0, 0, f"{value:.2f}", horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')

def display_circles(mean_rating, mean_similarity):
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    
    # Plot mean rating
    axs[0].set_title("Mean Rating")
    plot_circle(axs[0], mean_rating, max_value=5)  # Normalize mean_rating to be between 0 and 1
    axs[0].set_xlim(-1.2, 1.2)
    axs[0].set_ylim(-1.2, 1.2)
    axs[0].set_aspect('equal')
    axs[0].axis('off')
    
    # Plot mean similarity
    axs[1].set_title("Mean Agreement")
    plot_circle(axs[1], mean_similarity)
    axs[1].set_xlim(-1.2, 1.2)
    axs[1].set_ylim(-1.2, 1.2)
    axs[1].set_aspect('equal')
    axs[1].axis('off')

    # Add a legend
    legend_elements = [
        Patch(facecolor='blue', edgecolor='black', label='Great Agreement (>= 0.8)'),
        Patch(facecolor='green', edgecolor='black', label='Mostly Agreement (0.6 - 0.8)'),
        Patch(facecolor='orange', edgecolor='black', label='Low Agreement (0.3 - 0.6)'),
        Patch(facecolor='red', edgecolor='black', label='Conflict (< 0.3)'),
    ]

    # Create a legend
    plt.legend(handles=legend_elements, bbox_to_anchor=(1.5, 1))

    plt.tight_layout()
    plt.show()

""" #Example usage
mean_rating = 3.3  # Example mean rating out of 5
mean_similarity = 0.55  # Example mean similarity score out of 1
display_circles(mean_rating, mean_similarity)"""