import  numpy as np
import random
import time
import matplotlib.pyplot as plt

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


def depth_first(maze,start,end):
    st=time.perf_counter()
    #maze=np.array(maze)
    #maze[maze==-2]=0
    #maze[maze==-3]=0
    row,col=maze.shape
    stack=[(start,[start])]
    directions=[(0,1),(1,0),(0,-1),(-1,0)]#right,down,left,up this tottlay depend on which direction robot move so just remember if you choose one as right (0,1)
    #then the left surly will be (0,-1)
    visited=set()

    while stack:
        (x,y),path=stack.pop()
        if (x,y)==end:
            et=time.perf_counter()
            tt=et-st
            visited.add(end)
            return path,tt,visited

        if (x,y) not in visited:
            visited.add((x,y))
            for dx,dy in directions:
                nx=x+dx
                ny=y+dy
                try:
                    condition1=maze[nx,ny]==0 or maze[nx,ny]==-2 or maze[nx,ny]==-3
                except IndexError as er:
                    pass
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited:
                    if condition1:
                       stack.append(((nx,ny),path+[(nx,ny)]))

    return None


def main():
    maze=generateMap2d([5,5])
    print(maze)
    #maze1=maze.copy()
    maze=np.array(maze)
    #mazec=maze.__copy__()
    st_r,st_c=np.where(maze==-2)
    en_r,en_c=np.where(maze==-3)
    start=(int(st_r[0]),int(st_c[0]))
    end=(int(en_r[0]),int(en_c[0]))
    result,total_time,visited=depth_first(maze,start,end)
    print(f"Result: {result}\t it took: {total_time} visited nodes: {visited}")
    #print(maze.shape)
    for x,y in result:
        if not (maze[x,y]==-3 or maze[x,y]==-2):
            maze[x,y]=2
    print(maze)
    plt.figure()
    plt.imshow(maze,interpolation='nearest')
    plt.colorbar()
    plt.show()



if __name__=='__main__':
    main()



