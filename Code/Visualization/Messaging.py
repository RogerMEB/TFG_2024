import matplotlib.pyplot as plt
import matplotlib.patches as patches

def display_message_box(title, message, message_type='info'):
    fig, ax = plt.subplots(figsize=(6, 4))

    # Determine the background color based on message type
    if message_type == 'alert':
        box_color = 'salmon'
        symbol = '⚠️'
        symbol_color = 'red'
    elif message_type == 'positive':
        box_color = 'lightgreen'
        symbol = '✔️'
        symbol_color = 'green'
    else:
        box_color = 'lightblue'
        symbol = 'ℹ️'
        symbol_color = 'blue'

    # Draw a rectangle for the message box
    box = patches.FancyBboxPatch((0.1, 0.1), 0.8, 0.8,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='black',
                                 facecolor=box_color)
    ax.add_patch(box)

    # Add the title
    plt.text(0.5, 0.75, title, fontsize=15, fontweight='bold', ha='center', va='center')

    # Add the message text
    plt.text(0.5, 0.5, message, fontsize=12, ha='center', va='center')

    # Add the symbol
    plt.text(0.9, 0.9, symbol, fontsize=20, ha='center', va='center', color=symbol_color)

    # Remove axes
    ax.axis('off')

    plt.show()

"""# Example usage
display_message_box('Conflictive Groups Detected', '\nThe following groups have noticeable high conflict:\n\n Group 3, Group 6, Group 11, Group 12\n\n\n\n Select them for more detail', 'alert')
display_message_box('High Agreement Accross Groups', 'The valuations between students as well as the\n overall ratings are largely positive.\n80% of the groups have a positive scores.\n\n The evaluation and improvement phase\n have progressed with concordence.', 'positive')
display_message_box('Report', '\n\n\n- Student A strongly disagrees with Student D\n\n- Student B strongly disagrees with Student F\n\n- Student C strongly disagrees with Student H\n\n- Student D strongly disagrees with Student E \n\n Click to see the answers', 'info')"""
