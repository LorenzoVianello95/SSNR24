import numpy as np
from scipy.signal import argrelextrema
from scipy.interpolate import interp1d


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

def segment_stride(stance_interpolate_factor, joint, segment_length=100):
    """
    Segments gait using stance interpolation factor.

    """
    segments_alpha = []
    segments_theta = []
    start_index = 0
    completed_gait = False

    for i in range(1, len(stance_interpolate_factor)):
        if stance_interpolate_factor[i] == 1:
            completed_gait = True
        elif completed_gait and stance_interpolate_factor[i] == 0:
            segments_alpha.append(stance_interpolate_factor[start_index:i])
            segments_theta.append(joint[start_index:i])
            start_index = i
            completed_gait = False

    interpolated_segments_alpha = []
    interpolated_segments_theta = []
    for segment_al, segment_th in zip(segments_alpha, segments_theta):
        if len(segment_al)< 900:
            x = np.linspace(0, 1, len(segment_al))
            f = interp1d(x, segment_al, kind='linear')
            x_new = np.linspace(0, 1, segment_length)
            interpolated_segments_alpha.append(f(x_new))
            
            x = np.linspace(0, 1, len(segment_th))
            f = interp1d(x, segment_th, kind='linear')
            interpolated_segments_theta.append(f(x_new))

    return np.array(interpolated_segments_alpha), np.array(interpolated_segments_theta)
