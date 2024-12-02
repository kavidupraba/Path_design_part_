import numpy as np


def heuristic(current_n, goal_n, trow, brow, mcol, typeh="manhattan", move=(0, 1)):
    LARGE_VALUE = 1e6  # Replace 'inf' with a large value

    print(f"Current Node: {current_n}, Goal Node: {goal_n}, Move: {move}")
    print(f"Trow: {trow}, Brow: {brow}, Mcol: {mcol}")

    # Calculate magnitude based on the heuristic type
    difference_v = np.array(current_n) - np.array(goal_n)
    if typeh == "manhattan":
        magnitude = np.linalg.norm(difference_v, ord=1)
    else:
        magnitude = np.linalg.norm(difference_v, ord=2)
    print(f"Calculated Magnitude: {magnitude}")

    x, y = current_n
    gx, gy = goal_n

    top_row_of_h = brow
    bottom_row_of_h = trow
    midd_c_of_h = mcol

    # Define conditions
    condition1 = top_row_of_h < y < midd_c_of_h < gy#if map is 60x60 row count=col count
    condition2 = top_row_of_h < x < bottom_row_of_h

    print(f"Condition1: {condition1}, Condition2: {condition2}")

    # Map moves to directions
    mapping = {
        (0, 1): "right",
        (0, -1): "left",
        (-1, 0): "up",
        (1, 0): "down"
    }
    move_n = mapping.get(move)
    print(f"Move Direction: {move_n}")

    # Handle conditions and movements
    if condition1:
        di_f_top = abs(top_row_of_h - x)
        di_f_bottom = abs(bottom_row_of_h - x)
        condition3 = di_f_bottom > di_f_top
        print(f"Condition3: {condition3}")
        if condition2:
            match move_n:
                case "right":
                    return LARGE_VALUE
                case "left":
                    return magnitude
                case "up":
                    #return magnitude - top_row_of_h if condition3 else magnitude + bottom_row_of_h
                    return magnitude + bottom_row_of_h if condition3 else magnitude - top_row_of_h
                case "down":
                    #return magnitude + bottom_row_of_h if condition3 else magnitude - top_row_of_h
                    return magnitude - top_row_of_h if condition3 else magnitude + bottom_row_of_h
        else:
            return magnitude
    elif x < top_row_of_h:
        di_f_top = abs(top_row_of_h - x)
        di_f_bottom = abs(bottom_row_of_h - x)
        condition3 = di_f_bottom > di_f_top
        print(f"Condition3 (vertical): {condition3}")
        if move_n in ["up", "down"]:
            if move_n == "up" and condition3:
                return 0
            return LARGE_VALUE if condition3 else 0
    else:
        print("Warning: Heuristic fell through all conditions. Defaulting to magnitude.")
        return magnitude

    return magnitude
