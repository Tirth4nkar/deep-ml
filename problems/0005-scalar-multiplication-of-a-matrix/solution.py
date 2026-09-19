def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	for row in matrix:
		for element_idx in range(len(row)):
			row[element_idx] = row[element_idx]*scalar
	return matrix