import heapq
import time
from special_heuristic import heuristic
from map_and_plot import *
from A_star_algorithm import A_stare_algorithm

def A_star_algorithm2(maze, start, end, trow, brow, mcol, typeh="manhattan"):
    """
    A* algorithm implementation with a custom heuristic function.

    Parameters:
        maze (np.ndarray): The grid representing the maze.
        start (tuple): The starting coordinates (x, y).
        end (tuple): The goal coordinates (x, y).
        trow (int): Top row limit for heuristic considerations.
        brow (int): Bottom row limit for heuristic considerations.
        mcol (int): Middle column limit for heuristic considerations.
        typeh (str): Type of heuristic to use ("manhattan" or other).

    Returns:
        tuple: (path, total_time, fn, gn, hn, visited_nodes)
    """
    st = time.perf_counter()
    row, col = maze.shape
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = []
    visited = set()
    parents = {}

    # Initial heuristic value
    initial_hn = heuristic(start, end, trow, brow, mcol, typeh)
    heapq.heappush(pq, (0 + initial_hn, 0, initial_hn, start))

    while pq:
        fn, gn, hn, current_node = heapq.heappop(pq)

        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents.get(current_node)
            path.reverse()
            et = time.perf_counter()
            total_time = et - st
            return path, total_time, fn, gn, hn, visited

        if current_node not in visited:
            visited.add(current_node)
            for dx, dy in directions:
                nx, ny = current_node[0] + dx, current_node[1] + dy
                if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited and maze[nx, ny] != -1:
                    move = (dx, dy)
                    new_gn = gn + 1
                    hn = heuristic((nx, ny), end, trow, brow, mcol, typeh, move)
                    fn = new_gn + hn
                    heapq.heappush(pq, (fn, new_gn, hn, (nx, ny)))
                    parents[(nx, ny)] = current_node

    # If no path is found
    return None, None, None, None, None, None

def main():
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
    print("one with weighted h(n)")

    print("A STAR ALGORITHM")
    print("**********************manhattan*****************************")
    result, total_time, fn, gn, hn, visited2_1 = A_star_algorithm2(maze, start, end,ytop,ybot,minx,typeh="manhattan")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited2_1}")
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")
    # total cost function keep track of all the cost f(n)
    # keep track of past cost g(n) cost function
    # telling about remaining cost to goal h(n) heuristic function
    print("*********************euclidean******************************")
    result, total_time, fn, gn, hn, visited2_2 = A_star_algorithm2(maze, start, end,ytop,ybot,minx, typeh="euclidean")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited2_2}")
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")
    print("one with normal h(n)")

    print("A STAR ALGORITHM")
    print("**********************manhattan*****************************")
    result, total_time, fn, gn, hn, visited1_1 = A_stare_algorithm(maze, start, end, typeh="manhattan")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited1_1}")
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")
    # total cost function keep track of all the cost f(n)
    # keep track of past cost g(n) cost function
    # telling about remaining cost to goal h(n) heuristic function
    print("*********************euclidean******************************")
    result, total_time, fn, gn, hn, visited1_2 = A_stare_algorithm(maze, start, end, typeh="euclidean")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited1_2}")
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")
        print(f"one with new heuristic expanded nod count for manhattan+weighted: {len(visited2_1)}")
        print(f"one with new heuristic expanded nod count for euclidian+weighted: {len(visited2_2)}")
        print(f"one with old heuristic expanded nod count for manhattan: {len(visited1_1)}")
        print(f"one with old heuristic expanded nod count for euclidian: {len(visited1_2)}")


if __name__=='__main__':
    main()