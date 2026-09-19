import numpy as np

def get_eigenvalues(trace: float, det: float) -> list[float]:
    term = np.sqrt(trace**2 - 4 * det)
    lambda1 = (trace + term) / 2
    lambda2 = (trace - term) / 2
    
    # Return sorted from highest to lowest
    return [float(lambda1), float(lambda2)]

def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    # summing the main diagonal
	trace_val = matrix[0][0] + matrix[1][1]
    # Calculate determinant for a 2x2 matrix: (a*d - b*c)
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    return get_eigenvalues(trace=trace_val, det=det)