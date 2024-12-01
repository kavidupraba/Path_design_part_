import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Random_agent import random_agent
from dfs_search import depth_first
from breadth_first_search import finding_the_shortest_path
from greed_breadth_first import gbf
from A_star_algorithm import A_stare_algorithm
from map_and_plot import *
from record import record1,record2



def main():
    print("Normal obstetrical map")
    maze = generateMap2d([60, 60])
    maze = np.array(maze)
    s_row, s_col = np.where(maze == -2)
    e_row, e_col = np.where(maze == -3)
    start = (int(s_row[0]), int(s_col[0]))
    end = (int(e_row[0]), int(e_col[0]))
    print(maze)
    print("RANDOM AGENT")
    result, timet, visited = random_agent(maze, start, end)
    if result is None:
        print("No result no valid path")
    else:
        print(f"{result} and it took: {timet} visited nodes: {visited}\n\n")
        record1("random",result,timet,visited=visited)
        plotMap(maze, np.array(result), title_="Random Agent Path on Normal Map")

    print("BREADTH FIRST SEARCH")
    result, total_time, visited = finding_the_shortest_path(maze, start, end)
    if result is None:
        print("No result no valid path")
    else:
        print(f"path: {result}\t time it took: {total_time} visited nodes: {visited}\n\n")
        record1("BREADTH FIRST SEARCH", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="BREADTH FIRST agent (uninformed)  Path on Normal Map")

    print("DEPTH FIRST SEARCH")
    result, total_time, visited = depth_first(maze, start, end)
    if result is None:
        print("No result no valid path")
    else:
        print(f"Result: {result}\t it took: {total_time} visited nodes: {visited}\n\n")
        record1("DEPTH FIRST SEARCH", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="DEPTH FIRST SEARCH agent (uninformed)  Path on Normal Map")


    print("GREEDY BREADTH FIRST SEARCH")
    print("*********************manhattan***********************")
    result, total_time, visited = gbf(maze, start, end, "manhattan")
    if result is None:
        print("No path found!")
    else:
        print(f"Result: {result}\t it took: {total_time} visited nodes: {visited}\n\n")
        record1("GREEDY BREADTH FIRST SEARCH MANHATTAN", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="GREEDY BREADTH FIRST SEARCH agent (informed)  Path on Normal Map Euclidian distance")

    print("*********************euclidean***********************")
    result, total_time, visited = gbf(maze, start, end, "euclidean")
    if result is None:
        print("No path found!")
    else:
        print(f"Result: {result}\t it took: {total_time} visited nodes: {visited}\n\n")
        record1("GREEDY BREADTH FIRST SEARCH EUCLIDEAN", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="GREEDY BREADTH FIRST SEARCH agent (informed)  Path on Normal Map Manhattan distance")

    print("A STAR ALGORITHM")
    print("**********************manhattan*****************************")
    result, total_time, fn, gn, hn, visited = A_stare_algorithm(maze, start, end, typeh="manhattan")
    if result is None:
        print("No path found!")
    else:
       print(f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited} Euclidian distance")
       record1("A STAR ALGORITHM MANHATTAN", result, total_time,fn=fn,gn=gn,hn=hn,visited=visited)
       plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed)  Path on Normal Map")
    # total cost function keep track of all the cost f(n)
    # keep track of past cost g(n) cost function
    # telling about remaining cost to goal h(n) heuristic function
    print("*********************euclidean******************************")
    result, total_time, fn, gn, hn, visited = A_stare_algorithm(maze, start, end, typeh="euclidean")
    if result is None:
        print("No path found!")
    else:
        record1("A STAR ALGORITHM EUCLIDEAN", result, total_time, fn=fn, gn=gn, hn=hn, visited=visited)
        print(f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited} Manhattan distance")
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed)  Path on Normal Map")

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



    print("RANDOM AGENT")
    result, timet, visited = random_agent(maze, start, end)
    if result is None:
        print("No result no valid path")
    else:
        print(f"{result} and it took: {timet} visited nodes: {visited}\n\n")
        plotMap(maze, np.array(result), title_="Random Agent Path on H Shape Map")
        record2("random", result, timet, visited=visited)

    print("BREADTH FIRST SEARCH")
    result, total_time, visited = finding_the_shortest_path(maze, start, end)
    if result is None:
        print("No result no valid path")
    else:
        print(f"path: {result}\t time it took: {total_time} visited nodes: {visited}\n\n")
        record2("BREADTH FIRST SEARCH", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="BREADTH FIRST agent (uninformed) Path on H Shape Map")

    print("DEPTH FIRST SEARCH")
    result, total_time, visited = depth_first(maze, start, end)
    if result is None:
        print("No result no valid path")
    else:
        print(f"Result: {result}\t it took: {total_time} visited nodes: {visited}\n\n")
        record2("DEPTH FIRST SEARCH", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="DEPTH FIRST SEARCH agent (uninformed) Path on H Shape Map")

    print("GREEDY BREADTH FIRST SEARCH")
    print("*********************manhattan***********************")
    result, total_time, visited = gbf(maze, start, end, "manhattan")
    if result is None:
        print("No path found!")
    else:
        print(f"Result: {result}\t it took: {total_time} visited nodes: {visited}\n\n")
        record2("GREEDY BREADTH FIRST SEARCH MANHATTAN", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="GREEDY BREADTH FIRST SEARCH agent (informed) Path on H Shape Map")

    print("*********************euclidean***********************")
    result, total_time, visited = gbf(maze, start, end, "euclidean")
    if result is None:
        print("No path found!")
    else:
        print(f"Result: {result}\t it took: {total_time} visited nodes: {visited}\n\n")
        record2("GREEDY BREADTH FIRST SEARCH EUCLIDEAN", result, total_time, visited=visited)
        plotMap(maze, np.array(result), title_="GREEDY BREADTH FIRST SEARCH agent (informed) Path on H Shape Map")

    print("A STAR ALGORITHM")
    print("**********************manhattan*****************************")
    result, total_time, fn, gn, hn, visited = A_stare_algorithm(maze, start, end, typeh="manhattan")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited}")
        record2("A STAR ALGORITHM MANHATTAN", result, total_time, fn=fn, gn=gn, hn=hn, visited=visited)
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")
    # total cost function keep track of all the cost f(n)
    # keep track of past cost g(n) cost function
    # telling about remaining cost to goal h(n) heuristic function
    print("*********************euclidean******************************")
    result, total_time, fn, gn, hn, visited = A_stare_algorithm(maze, start, end, typeh="euclidean")
    if result is None:
        print("No path found!")
    else:
        print(
            f"Path: {result} it took {total_time} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited}")
        record2("A STAR ALGORITHM EUCLIDEAN", result, total_time, fn=fn, gn=gn, hn=hn, visited=visited)
        plotMap(maze, np.array(result), title_="A STAR ALGORITHM agent (informed) Path on H Shape Map")




if __name__ == "__main__":
    main()
