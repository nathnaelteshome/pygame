import numpy as np

def show_determinant(array):
    # Calculate the determinant of the matrix
    determinant = np.linalg.det(array)
    
    return determinant
# Example usage
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = show_determinant(my_array)
print(result)
