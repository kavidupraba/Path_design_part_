import numpy as np
import random
import time
import matplotlib.pyplot as plt
import pandas as pd

percentOfObstacle = 1  # 30% - 60%, random
def generateMap2d(size_):
    global percentOfObstacle
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



def random_agent(maze,start,end):
    step=0
    st=time.perf_counter()
    maze=np.array(maze)
    row,col=maze.shape
    directions=[(0,1),(1,0),(0,-1),(-1,0)]#right,down,left,up
    r_list=[(start,[start])]
    visited=set()

    while r_list:
        (x,y),path=r_list.pop()
        if (x,y)==end:
            et=time.perf_counter()
            ft=et-st
            visited.add(end)
            return path,ft,visited

        random.shuffle(directions)
        if (x,y)  not in visited:
            visited.add((x,y))
            step += 1
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<row and 0<=ny<col and maze[nx,ny]!=-1:
                r_list.append([(nx,ny),path+[(nx,ny)]])# add new path
                #I'm gonna add fail safe method to jump from this loop if I explore too much
                if step>=100:
                    break#this will stop expanding nodes after 100 visited only expand ro one side


        #if step>=row*col*2:
        #break

    return None,None,None


def main():
    maze=generateMap2d([5,5])
    maze=np.array(maze)
    start_row,start_col=np.where(maze==-2)
    end_row,end_col=np.where(maze==-3)
    start=(int(start_row[0]),int(start_col[0]))
    end=(int(end_row[0]),int(end_col[0]))
    result,timet,visited=random_agent(maze,start,end)
    print(f"{result} and it took: {timet} visited nodes: {visited}")
    print(maze)

    #fig,ax=plt.subplots(1,2,sharey=True,)

if __name__=='__main__':
    main()

