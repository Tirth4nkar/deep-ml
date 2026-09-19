import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == "row":
		means = [np.mean(row).item() for row in matrix]
		return means
	
	means = [[row[col_idx] for row in matrix]for col_idx in range(len(matrix[0]))]
	means = [np.mean(col).item() for col in means]
	return means