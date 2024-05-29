import numpy as np
from scipy.signal import argrelextrema


def find_local_maxima(array, num_maxima):
    """
    Finds the specified number of local maxima in the array.

    Parameters:
    - array: The 1-D array representing the function.
    - num_maxima: The number of local maxima to find.

    Returns:
    - local_maxima_indices: Indices of the local maxima in the array.
    """
    # Find the indices of local maxima
    local_maxima_indices = argrelextrema(array, np.greater, order=10)[0]  # Adjust order as needed for local maximum detection

    # Sort the local maxima by their corresponding values
    sorted_indices = local_maxima_indices[np.argsort(array[local_maxima_indices])[::-1]]

    # Return the specified number of local maxima
    return sorted_indices[:num_maxima]