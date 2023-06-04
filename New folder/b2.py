import numpy as np

def decompose_matrices(array):
    # Perform Singular Value Decomposition
    U, S, V = np.linalg.svd(array)
    
    # Decompose the matrices
    diagonal_matrix = np.diag(S)
    decomposed_matrices = [U, diagonal_matrix, V]
    
    return decomposed_matrices
# Example usage
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = decompose_matrices(my_array)
print(result)
