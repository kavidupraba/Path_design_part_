import time

import numpy as np
import random
import matplotlib.pyplot
import heapq
#from collections import deque

#in here we calculate g(n) value by 1 mark for each (travalable node ) and starting nod is 0

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

def heuristic(current_n,goal_n,typeh="manhattan"):
    '''
    :param current_n: current position of the bot (current node)
    :param goal_n: goal node (where goal alies)
    :return:heuristic value (manhattan distance) /manhattan norm
    '''
    difference = np.array(goal_n) - np.array(current_n)
    match type:
        case "manhattan":
            magnitude=np.linalg.norm(difference,ord=1)
        case "euclidean":
            magnitude = np.linalg.norm(difference, ord=2)
        case _:
            magnitude = np.linalg.norm(difference, ord=1)
    return magnitude


def A_stare_algorithm(maze,start,end,typeh="manhattan"):
    st=time.perf_counter()
    row,col=maze.shape
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    pq=[]
    visited=set()
    parents={}#parents={start:None}
    heapq.heappush(pq,(0+heuristic(start,end,typeh),0,heuristic(start,end,typeh),start))
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
            visited.add(end)
            return path,tt,fn,gn,hn,visited

        if current_node not in visited:
            visited.add(current_node)
            for dx,dy in directions:
                nx,ny=current_node[0]+dx,current_node[1]+dy
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited and maze[nx,ny]!=-1:
                    new_gn=gn+1
                    hn=heuristic((nx,ny),end,typeh)
                    fn=new_gn+hn
                    heapq.heappush(pq,(fn,new_gn,hn,(nx,ny)))
                    parents[(nx,ny)]=current_node
    return None,None,None,None,None,None

def main():
    maze=generateMap2d([5,5])
    maze=np.array(maze)
    s_row,s_col=np.where(maze==-2)
    e_row,e_col=np.where(maze==-3)
    start=(int(s_row[0]),int(s_col[0]))
    end=(int(e_row[0]),int(e_col[0]))
    print(maze)
    print("**********************manhattan*****************************")
    path,tt,fn,gn,hn,visited=A_stare_algorithm(maze,start,end,typeh="manhattan")
    print(f"Path: {path} it took {tt} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited}")
    #total cost function keep track of all the cost f(n)
    #keep track of past cost g(n) cost function
    #telling about remaining cost to goal h(n) heuristic function
    print("*********************euclidean******************************")
    path, tt, fn, gn, hn,visited = A_stare_algorithm(maze, start, end, typeh="euclidean")
    print(f"Path: {path} it took {tt} f(n)=h(n)+g(n) total cost function:{fn} g(n) past cost/growth function:{gn} h(n) heuristic function:{hn} visited nodes: {visited}")


if __name__=='__main__':
    main()