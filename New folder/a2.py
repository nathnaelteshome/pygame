import numpy as np

def compute_cross_product(arr1, arr2):
    cross_product = np.cross(arr1, arr2)
    return cross_product
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = compute_cross_product(arr1, arr2)
print(result)  # Output: [-3  6 -3]
