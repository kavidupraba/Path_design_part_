import numpy as np
import time
import heapq
from special_heuristic2 import heuristic
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# helper function for plotting the result
def plotMap(map2d_, path_, title_=''):
    '''Plots a map (image) of a 2d matrix with a path from start point to the goal point.
        cells with a value of 0: Free cell;
                             -1: Obstacle;
                             -2: Start point;
                             -3: Goal point;
    Parameters:
    -----------
    map2d_ : array-like
        an array with Real Numbers

    path_ : array-like
        an array of 2d corrdinates (of the path) in the format of [[x0, y0], [x1, y1], [x2, y2], ..., [x_end, y_end]]

    title_ : string
        information/description of the plot

    Returns:
    --------

    '''

    import matplotlib.cm as cm
    plt.interactive(False)

    colors_nn = int(map2d_.max())
    colors = cm.winter(np.linspace(0, 1, colors_nn))

    colorsMap2d = [[[] for x in range(map2d_.shape[1])] for y in range(map2d_.shape[0])]
    # Assign RGB Val for starting point and ending point
    locStart, locEnd = np.where(map2d_ == -2), np.where(map2d_ == -3)

    colorsMap2d[locStart[0][0]][locStart[1][0]] = [.0, .0, .0, 1.0]  # black
    colorsMap2d[locEnd[0][0]][locEnd[1][0]] = [.0, .0, .0, .0]  # white

    # Assign RGB Val for obstacle
    locObstacle = np.where(map2d_ == -1)
    for iposObstacle in range(len(locObstacle[0])):
        colorsMap2d[locObstacle[0][iposObstacle]][locObstacle[1][iposObstacle]] = [1.0, .0, .0, 1.0]
    # Assign 0
    locZero = np.where(map2d_ == 0)

    for iposZero in range(len(locZero[0])):
        colorsMap2d[locZero[0][iposZero]][locZero[1][iposZero]] = [1.0, 1.0, 1.0, 1.0]

    # Assign Expanded nodes
    locExpand = np.where(map2d_ > 0)

    for iposExpand in range(len(locExpand[0])):
        _idx_ = int(map2d_[locExpand[0][iposExpand]][locExpand[1][iposExpand]] - 1)
        colorsMap2d[locExpand[0][iposExpand]][locExpand[1][iposExpand]] = colors[_idx_]

    for irow in range(len(colorsMap2d)):
        for icol in range(len(colorsMap2d[irow])):
            if colorsMap2d[irow][icol] == []:
                colorsMap2d[irow][icol] = [1.0, 0.0, 0.0, 1.0]

    path = path_.T.tolist()

    plt.figure()
    plt.title(title_)
    plt.imshow(colorsMap2d, interpolation='nearest')
    plt.colorbar()
    plt.plot(path[:][0], path[:][1], color='magenta', linewidth=2.5)
    plt.show()
def plotMap1(map2d_, path_, title_=''):
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
    plt.figure(figsize=(8, 8))
    plt.title(title_)
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
    plt.legend(handles=legend_patches, loc='upper right', fontsize=8)

    # Display the grid
    plt.grid(visible=True, which='both', color='gray', linewidth=0.5, alpha=0.5)
    plt.xticks(range(map2d_.shape[1]))
    plt.yticks(range(map2d_.shape[0]))
    plt.gca().invert_yaxis()

    plt.colorbar(label="Node Value (if applicable)")
    plt.show()


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

def A_stare_algorithm(maze,start,end,trow,brow,mcol,typeh="manhattan"):
    st=time.perf_counter()
    row,col=maze.shape
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    pq=[]
    visited=set()
    parents={}#parents={start:None}
    heapq.heappush(pq,(0+heuristic(start,end,trow,brow,mcol,typeh),0,heuristic(start,end,trow,brow,mcol,typeh),start))
    while pq:
        fn,gn,hn,current_node=heapq.heappop(pq)
        if current_node==end:
            path=[]
            while current_node:
                path.append(current_node)
                current_node=parents.get(current_node)#if you use .get() insted parent[current_node] you will not going to face the issuse of
                # we not adding parents={start:None} before hand!
            path.reverse()
            et=time.perf_counter()
            tt=et-st
            return path,tt,fn,gn,hn,visited

        if current_node not in visited:
            visited.add(current_node)
            for dx,dy in directions:
                nx,ny=current_node[0]+dx,current_node[1]+dy
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited and maze[nx,ny]!=-1:
                    new_gn=gn+1
                    hn=heuristic((nx,ny),end,trow,brow,mcol,typeh)
                    fn=new_gn+hn
                    heapq.heappush(pq,(fn,new_gn,hn,(nx,ny)))
                    parents[(nx,ny)]=current_node
    return None,None,None,None,None,None

def main():
    print("H shape map here!*********************************************")
    size = [60, 60]  # Define map size
    map2d, hshape_info = generateMap2d_obstacle(size)
    maze = np.array(map2d)
    s_row, s_col = np.where(maze == -2)
    e_row, e_col = np.where(maze == -3)
    start = (int(s_row[0]), int(s_col[0]))
    end = (int(e_row[0]), int(e_col[0]))
    print(maze)

    ytop, ybot, minx = hshape_info
    print(f"Top Horizontal Wall (ytop): Row {ytop}")
    print(f"Bottom Horizontal Wall (ybot): Row {ybot}")
    print(f"Vertical Wall (minx): Column {minx}")



    print("A STAR ALGORITHM")
    print("**********************manhattan*****************************")
    result, total_time, fn, gn, hn, visited = A_stare_algorithm(maze, start, end,ytop, ybot, minx, typeh="manhattan")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited}")
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")
    # total cost function keep track of all the cost f(n)
    # keep track of past cost g(n) cost function
    # telling about remaining cost to goal h(n) heuristic function
    print("*********************euclidean******************************")
    result, total_time, fn, gn, hn, visited = A_stare_algorithm(maze, start, end,ytop, ybot, minx, typeh="euclidean")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited}")
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")


if __name__ == "__main__":
    main()
