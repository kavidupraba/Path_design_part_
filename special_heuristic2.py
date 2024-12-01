import numpy as np


def heuristic(current_n, goal_n, trow, brow, mcol, typeh="manhattan"):
    '''
    Custom heuristic function with penalties for navigating around the "H" wall.

    :param current_n: Current position of the bot (node)
    :param goal_n: Goal node position
    :param trow: y-coordinate of the top horizontal wall
    :param brow: y-coordinate of the bottom horizontal wall
    :param mcol: x-coordinate of the vertical wall
    :param typeh: Type of base heuristic ("manhattan" or "euclidean")
    :return: Heuristic value with penalties
    '''
    current_r, current_c = current_n  # current_r = current row (y), current_c = current column (x)
    goal_r, goal_c = goal_n  # goal_r = goal row (y), goal_c = goal column (x)

    # Base heuristic (distance to goal)
    difference = np.array([goal_r, goal_c]) - np.array([current_r, current_c])
    match typeh:
        case "manhattan":
            base_magnitude = np.linalg.norm(difference, ord=1)
        case "euclidean":
            base_magnitude = np.linalg.norm(difference, ord=2)
        case _:
            base_magnitude = np.linalg.norm(difference, ord=1)

    # Penalty for moving toward the vertical wall (minx)
    penalty = 0
    if brow <= current_r <= trow and current_c == mcol:
        penalty += 10  # Strong penalty for moving directly into the vertical wall

    # Encourage vertical movement (upward or downward) by reducing penalties
    if current_r < brow:
        penalty -= abs(brow - current_r)  # Reduce heuristic value if moving downward
    elif current_r > trow:
        penalty -= abs(current_r - trow)  # Reduce heuristic value if moving upward

    return base_magnitude + penalty
