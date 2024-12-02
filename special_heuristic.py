import numpy as np

'''
Top Horizontal Wall (ytop): Row 51
Bottom Horizontal Wall (ybot): Row 7
Vertical Wall (minx): Column 29
'''
def heuristic(current_n,goal_n,trow,brow,mcol,typeh="manhattan",move=(0,1)):
    difference_v=np.array(current_n)-np.array(goal_n)
    match typeh:
        case "manhattan":
            magnitude=np.linalg.norm(difference_v,ord=1)
        case _:
            magnitude = np.linalg.norm(difference_v, ord=2)
    x=current_n[0]
    y=current_n[1]

    gx=goal_n[0]
    gy=goal_n[1]

    top_row_of_h=brow#7
    bottom_row_of_h=trow#51
    midd_c_of_h=mcol

    mapping={
    (0, 1): "right",
    (0, -1): "left",
    (-1, 0): "up",
    (1, 0): "down"
}

    condition1=top_row_of_h<y<midd_c_of_h<gy
    #condition2=y<top_row_of_h#if the map is square shape ex: [60x60] row_count=col_count and top_row_of_h=top_row_of_y(at least close) if H design dosen't change
    # we can simplify this to top_row_of_h<y<midd_c_of_h<gy
    condition2=top_row_of_h<x<bottom_row_of_h
    move_n = mapping.get(move)

    if condition1:
        di_f_top=abs(top_row_of_h-x)
        di_f_bottom=abs(bottom_row_of_h-x)
        condition3=di_f_bottom>di_f_top
        if condition2:
            match move_n:
                case "right":
                    return float('inf')
                case "left":
                    return magnitude
                case "up":
                    if condition3:
                        return magnitude-top_row_of_h
                    else:
                        return magnitude+bottom_row_of_h
                case "down":
                        if condition3:
                            return magnitude + bottom_row_of_h
                        else:
                            return magnitude - top_row_of_h
        else:
            return magnitude
    elif x<top_row_of_h:
        if move_n=="up" or move_n=="down":
            di_f_top = abs(top_row_of_h - x)
            di_f_bottom = abs(bottom_row_of_h - x)
            condition3 = di_f_bottom > di_f_top
            if move_n=="up" and condition3:
                return 0
            else:
                if condition3:
                    return float('inf')
                else:
                    return 0
    else:
        return magnitude

"""
 a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b = np.array([3,4,7])
>>> c = np.setdiff1d(a,b)
"""