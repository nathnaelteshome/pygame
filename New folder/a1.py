import numpy as np

def show_dimension(arr):
    num_dimensions = np.ndim(arr)
    return num_dimensions
arr1 = np.array([1, 2, 3, 4, 5])
print(show_dimension(arr1))  # Output: 1

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(show_dimension(arr2))  # Output: 2

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(show_dimension(arr3))  # Output: 3
