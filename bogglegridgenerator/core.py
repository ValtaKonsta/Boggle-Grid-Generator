#Copy-pasted example app logic

import numpy as np

def generate_grid(rows, cols):
    """Generate a simple numeric grid."""
    return np.arange(rows * cols).reshape(rows, cols)
