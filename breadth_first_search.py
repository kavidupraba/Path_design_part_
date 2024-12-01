import time

import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from collections import deque
#from path_planning import generateMap2d


#a=list(range(1,5))
#print(a)
#print(a.shape)
#a=np.array(a)
#row=a.shape
#print(row)

percentOfObstacle = 1  # 30% - 60%, random


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

def finding_the_shortest_path(maze,start,end):
    #maze=np.array(maze)
    #maze[maze == -2] = 0
    #maze[maze == -3] = 0
    st=time.perf_counter()
    row_in,col_in=np.indices(maze.shape)
    row=len(row_in)
    col=len(col_in)
    directions=[(0,1),(1,0),(0,-1),(-1,0)]#right ,down, left ,up tuple inside a list tuples are iterative even in this form so we can unpack easily
    queue=deque([((start),[start])])
    visited=set()
    while queue:
        (x,y),path=queue.popleft()
        if (x,y)==end:
            et=time.perf_counter()
            tt=et-st
            visited.add(end)
            return path,tt,visited

        if (x,y) not in visited:
            visited.add((x,y))
            for dx,dy in directions:
                nx=dx+x
                ny=dy+y
                if 0<=nx<row and 0<=ny<col and maze[nx,ny]!=-1 and (nx,ny) not in visited:
                    queue.append(((nx,ny),path+[(nx,ny)]))

    return None


def main():
    map=generateMap2d([5,5])
    maze=np.array(map)
    s_row, s_col = np.where(maze == -2)
    start = (int(s_row[0]), int(s_col[0]))
    e_row, e_col = np.where(maze == -3)
    end = (int(e_row[0]), int(e_col[0]))
    #maze1=maze.__copy__()
    result,total_time,visited=finding_the_shortest_path(maze,start,end)
    if result is None:
        print("No result no valid path")
        return
    print(f"path: {result}\t time it took: {total_time} visited nodes: {visited}")
    for x,y in result:
        if maze[x,y] not in [-3,-2]:
            maze[x,y]=2
    print(f"{maze}")

    plt.figure()
    plt.imshow(maze,interpolation='nearest')
    plt.colorbar()
    plt.show()



if __name__=='__main__':
    main()


