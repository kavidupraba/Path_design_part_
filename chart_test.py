import matplotlib.pyplot as plt
import numpy as np

def draw_the_chart(maze, result):
    # Make a copy so we don't modify the original maze
    z = maze.copy()

    # Mark the path in the maze
    for i, j in result:
        if z[i, j] not in [-2, -3]:  # Don't overwrite start (-3) or end (-2)
            z[i, j] = 2  # Path marked as 2

    # Plot the maze using imshow
    plt.imshow(z, cmap="coolwarm", interpolation="nearest")

    # Add gridlines to see the blocks
    plt.grid(visible=True, color="black", linewidth=0.5)

    # Hide ticks for a cleaner grid
    plt.xticks([])  # No x-axis ticks
    plt.yticks([])  # No y-axis ticks

    # Add a title
    plt.title("Maze with Path (Simplified)")

    # Show the plot
    plt.show()

# Example maze and result
maze = np.array([
    [0, 0, -3, 1],
    [1, 1, 0, 1],
    [1, -2, 1, 1]
])
result = [(0, 2), (1, 2), (2, 1)]  # Example path

draw_the_chart(maze, result)
