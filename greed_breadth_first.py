import heapq
import time

import numpy
import matplotlib.pyplot as plt
import numpy as np
import math


percentOfObstacle = 1
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


def heuristic(c,e,type):
    c=np.array(c)
    e=np.array(e)
    difference=c-e
    match type:
        case "manhattan":
            manhattan_norm=np.linalg.norm(difference,ord=1)
            # we telling numpy to pick manhattan norm ||x||1=Σx=1 |xi| add n to the top !
            # h=abs(e[0]-c[0])+abs(e[1]-c[1])#manhaten distance OR MANHATTAN NORM! both are the same but remember ||A|| this is a norm
            # and this is |A| is absolute value and why Norm always should be bigger or equal to 0 (||A||>=0)BECAUSE THEIR IS no minus distances in real life
            # well you can say going back is minus but it's really not a minus we are the ones who decide it is minus or not
        case "euclidean":
           manhattan_norm = np.linalg.norm(difference, ord=2)#euclidean
        case _:
           manhattan_norm = np.linalg.norm(difference, ord=1)

    return manhattan_norm


def gbf(maze,start=(),end=(),heurist="manhattan"):
    '''
    :param maze: numpy array (the map)
    :param start: starting node (robot)
    :param end: end node (goal)
    :return: the path to the goal according to heuristic function (we calculate manhattan norm)
    '''
    st=time.perf_counter()
    #maze=np.array(maze)
    row,col=maze.shape
    #maze[maze==-2]=0
    #maze[maze==-3]=0
    directions=[(0,1),(1,0),(0,-1),(-1,0)]#right,down,left,up
    pq=[]#priority queue
    heapq.heappush(pq,(0,start))
    visited=set()
    previous_nods={}

    while pq:
        _,current_nod=heapq.heappop(pq)#pop the first in line object according to heuristic
        # we forget about heuristic because we need that to align the shortest path first in our list (priority queue)
        if current_nod==end:
            path=[]#path to the goal if current node is goal
            while current_nod:
                path.append(current_nod)
                current_nod=previous_nods.get(current_nod)#get the previous node before current node
                # ( in here we don't keep the whole track of the path like in bfs and dfs
            path.reverse()#we can also write this like path[::-1] remember that we also can copy list without .copy() using list_name[:]
            et=time.perf_counter()
            tt=et-st
            visited.add(end)
            return path,tt,visited

        if current_nod not in visited:
            visited.add(current_nod)#use set data structure to store visited nodes so we can stop useless roaming around
            for dx,dy in directions:
                nx,ny=current_nod[0]+dx,current_nod[1]+dy#add the directions to the node and get neighboring nods
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited and maze[nx,ny]!=-1:#check if calculated node is within our map row and col range
                    # and not in visited nod list
                    #if any(np.isin(maze[nx,ny],[0,-2,-3])):
                     #if not(maze[nx,ny]==-1):#check if current node value is representing a wall or not if not add to the priority queue
                     heapq.heappush(pq,(heuristic((nx,ny),end,heurist),(nx,ny)))
                     previous_nods[(nx,ny)]=current_nod# add the new nod as refference to current node

    return None,None,None

def draw_the_chart(maze,result):
    z=maze.__copy__()
    for i,j in result:
        if z[i,j] not in [-2,-3]:
            z[i,j]=2

    fig=plt.imshow(z,interpolation='nearest',label=[-3,-2])
    plt.legend()
    plt.grid()
    plt.title("Greedy breadth first search (heuristic=Manhattan Norm)")
    plt.show()


def main():
    maze=generateMap2d([5,5])
    maze=np.array(maze)
    print(maze)
    row_s,col_s=np.where(maze==-2)
    row_g,col_g=np.where(maze==-3)
    start=(int(row_s[0]),int(col_s[0]))
    end=(int(row_g[0]),int(col_g[0]))
    result,total_time,visited=gbf(maze,start,end,"manhattan")
    if result is None:
        print("No path found!")
        return
    print("*********************manhattan***********************")
    print(result)
    print(total_time)
    print(f"visited nodes: {visited}")
    print("*********************euclidean***********************")
    result,total_time,visited= gbf(maze, start, end, "euclidean")
    if result is None:
        print("No path found!")
        return
    print(result)
    print(total_time)
    print(f"visited nodes: {visited}")


    #draw_the_chart(maze,result)

if __name__=='__main__':
    main()








