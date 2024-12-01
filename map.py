import numpy as np
import matplotlib.pyplot as plt

# Create the map matrix
map_matrix = np.zeros((5, 5))  # Example: 5x5 grid
map_matrix[1, 2] = -2  # Robot at (1, 2)
map_matrix[3, 4] = -3  # Goal at (3, 4)

