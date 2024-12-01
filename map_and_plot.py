import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np

percentOfObstacle = 0.9  # 30% - 60%, random
def generateMap2d(size_):
    '''Generates a random 2d map with obstacles (small blocks) randomly distributed.
       You can specify any size of this map but your solution has to be independent of map size

    Parameters:
    -----------
    size_ : list
        Width and height of the 2d grid map, e.g. [60, 60]. The height and width of the map shall be greater than 20.

    Returns:
    --------
        map2d : array-like, shape (size_[0], size_[1])
           A 2d grid map, cells with a value of 0: Free cell;
                                                -1: Obstacle;
                                                -2: Start point;
                                                -3: Goal point;
    '''

    size_x, size_y = size_[0], size_[1]

    map2d = np.random.rand(size_y, size_x)
    perObstacles_ = percentOfObstacle
    map2d[map2d <= perObstacles_] = 0
    map2d[map2d > perObstacles_] = -1

    yloc, xloc = [np.random.randint(0, size_x - 1, 2), np.random.randint(0, size_y - 1, 2)]
    while (yloc[0] == yloc[1]) and (xloc[0] == xloc[1]):
        yloc, xloc = [np.random.randint(0, size_x - 1, 2), np.random.randint(0, size_y - 1, 2)]

    map2d[xloc[0]][yloc[0]] = -2
    map2d[xloc[1]][yloc[1]] = -3

    return map2d

# Generate 2d grid map with rotated-H-shape object
def generateMap2d_obstacle(size_):
    '''Generates a random 2d map with a rotated-H-shape object in the middle and obstacles (small blocks) randomly distributed.
       You can specify any size of this map but your solution has to be independent of map size

    Parameters:
    -----------
    size_ : list
        Width and height of the 2d grid map, e.g. [60, 60]. The height and width of the map shall be greater than 40.

    Returns:
    --------
        map2d : array-like, shape (size_[0], size_[1])
           A 2d grid map, cells with a value of 0: Free cell;
                                               -1: Obstacle;
                                               -2: Start point;
                                               -3: Goal point;

       [ytop, ybot, minx] : list
           information of the rotated-H-shape object
           ytop - y coordinate of the top horizontal wall/part
           ybot - y coordinate of the bottom horizontal wall/part
           minx - X coordinate of the vertical wall
    '''

    size_x, size_y = size_[0], size_[1]
    map2d = generateMap2d(size_)

    map2d[map2d == -2] = 0
    map2d[map2d == -3] = 0

    # add special obstacle
    xtop = [np.random.randint(5, 3 * size_x // 10 - 2), np.random.randint(7 * size_x // 10 + 3, size_x - 5)]
    ytop = np.random.randint(7 * size_y // 10 + 3, size_y - 5)
    xbot = np.random.randint(3, 3 * size_x // 10 - 5), np.random.randint(7 * size_x // 10 + 3, size_x - 5)
    ybot = np.random.randint(5, size_y // 5 - 3)

    map2d[ybot, xbot[0]:xbot[1] + 1] = -1
    map2d[ytop, xtop[0]:xtop[1] + 1] = -1
    minx = (xbot[0] + xbot[1]) // 2
    maxx = (xtop[0] + xtop[1]) // 2
    if minx > maxx:
        tempx = minx
        minx = maxx
        maxx = tempx
    if maxx == minx:
        maxx = maxx + 1

    map2d[ybot:ytop, minx:maxx] = -1
    startp = [np.random.randint(0, size_x // 2 - 4), np.random.randint(ybot + 1, ytop - 1)]

    map2d[startp[1], startp[0]] = -2
    goalp = [np.random.randint(size_x // 2 + 4, size_x - 3), np.random.randint(ybot + 1, ytop - 1)]

    map2d[goalp[1], goalp[0]] = -3
    # return map2d, [startp[1], startp[0]], [goalp[1], goalp[0]], [ytop, ybot]
    return map2d, [ytop, ybot, minx]




def plotMap(map2d_, path_, title_=''):
    """
    Plots a 2D maze with a path overlay.

    Parameters:
    -----------
    map2d_ : np.ndarray
        2D array representing the map where:
        0: Free cell,
        -1: Obstacle,
        -2: Start point,
        -3: Goal point.

    path_ : np.ndarray
        Array of 2D coordinates for the path, format: [[x0, y0], [x1, y1], ...]

    title_ : str
        Title of the plot.

    Returns:
    --------
    None
    """
    # Define the colormap for the map
    cmap = mcolors.ListedColormap(['white', 'black', 'red', 'blue', 'green'])
    bounds = [-3.5, -2.5, -1.5, -0.5, 0.5, map2d_.max() + 1]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Set up the plot
    plt.figure(figsize=(10, 7))  # Increased figure size for better visibility
    plt.title(title_, fontsize=16)  # Larger font size for the title
    plt.imshow(map2d_, cmap=cmap, norm=norm, origin='upper')

    # Plot the path (if provided)
    if path_ is not None and len(path_) > 0:
        path = np.array(path_)
        plt.plot(path[:, 1], path[:, 0], color='magenta', linewidth=2, label="Path")

    # Add a legend
    legend_labels = {
        "Start": -2,
        "Goal": -3,
        "Obstacle": -1,
        "Free cell": 0
    }
    legend_patches = [
        plt.Line2D([0], [0], marker='s', color='w', label=f"{label}",
                   markerfacecolor=cmap(norm(value)), markersize=10)
        for label, value in legend_labels.items()
    ]
    plt.legend(
        handles=legend_patches,
        loc='upper right',
        fontsize=10,
        frameon=True,
        bbox_to_anchor=(1.15, 1)  # Move the legend outside the plot
    )

    # Display the grid
    plt.grid(visible=True, which='both', color='gray', linewidth=0.5, alpha=0.5)

    # Adjust ticks
    step_x = max(1, map2d_.shape[1] // 20)  # Reduce x-ticks based on grid size
    step_y = max(1, map2d_.shape[0] // 20)  # Reduce y-ticks based on grid size
    plt.xticks(range(0, map2d_.shape[1], step_x), fontsize=8, rotation=45)  # Rotate x-tick labels

    # Reverse y-axis order
    y_ticks = range(0, map2d_.shape[0], step_y)  # Generate y-ticks with spacing
    reversed_y_ticks = list(reversed(y_ticks))  # Reverse the order of ticks

    plt.yticks(y_ticks, labels=reversed_y_ticks, fontsize=8)
 # Reverse the labels

    # Add a color bar
    cbar = plt.colorbar(label="Node Value (if applicable)")
    cbar.ax.tick_params(labelsize=10)  # Enlarge color bar labels

    plt.tight_layout()  # Adjust layout to prevent overlapping elements
    plt.show()


