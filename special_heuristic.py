import numpy as np

def heuristic(current_n,goal_n,trow,brow,mcol,typeh="manhattan",move=(0,1)):
    difference_v=np.array(current_n)-np.array(goal_n)
    match typeh:
        case "manhattan":
            magnitude=np.linalg.norm(difference_v,ord=1)
        case _:
            magnitude = np.linalg.norm(difference_v, ord=2)
    x=int(current_n[0])
    y=int(current_n[1])
    #I SAW THAT ROW NUMBER'S ARE DIFFERENT FOR THE ROW
    m_row=list(range(59,-1,-1))
    r_row=list(range(0,60,1))
    r_index=r_row.index(x)
    x=m_row[r_index]#this will fix the issue somewhat

    if mcol<y:
        if brow<x<trow:
            difference_from_top=trow-x
            difference_from_bot=abs(brow-x)
            if difference_from_top>difference_from_bot:#close to bottom
                match move:
                    case (1,0):#going down reduce the distance
                        magnitude=magnitude-difference_from_bot
                    case (-1,0):#going up discourage going up
                        magnitude=magnitude+difference_from_bot
                    case (0,1):#going right discourage going right
                        magnitude=magnitude+10
                    case (0,-1):#going left recode the distance
                        magnitude=magnitude-1
                    case _:
                        magnitude=magnitude

            else:#close to top
                match move:
                    case (1, 0):  # going down discourage going down
                        magnitude = magnitude + difference_from_top
                    case (-1, 0):  # going up reduce the distance
                        magnitude = magnitude - difference_from_top
                    case (0, 1):  # going right discourage going right
                        magnitude = magnitude + 10
                    case (0, -1):  # going left recode the distance
                        magnitude = magnitude - 1
                    case _:
                        magnitude = magnitude

        else:#x is bigger to =trow or smaller than=brow
            if x>=trow:#bigger or = to top
                match move:
                    case (1, 0):  # going down discourage going down
                        magnitude = magnitude + 10
                    case (-1, 0):  # going up do nothing
                        magnitude = magnitude
                    case (0, 1):  # going right reduce the dinstance
                        magnitude = magnitude -10
                    case (0, -1):  # going left give PENALTY!
                        magnitude = magnitude+5
                    case _:
                        magnitude = magnitude
            else:
                match move:
                    case (1, 0):  # going down do nothing
                        magnitude = magnitude
                    case (-1, 0):  # going up give penalty
                        magnitude = magnitude+10
                    case (0, 1):  # going right reduce the dinstance
                        magnitude = magnitude - 10
                    case (0, -1):  # going left give PENALTY!
                        magnitude = magnitude + 5
                    case _:
                        magnitude = magnitude
    else:
        magnitude=magnitude
    return magnitude

"""
 a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b = np.array([3,4,7])
>>> c = np.setdiff1d(a,b)
"""