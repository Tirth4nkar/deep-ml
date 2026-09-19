def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	prod_vec = []
	for row in a:

		if len(row)!=len(b):
			return  -1

		row_res = 0
		for element_idx in range(len(row)):
			row_res = row_res + row[element_idx]*b[element_idx]
		prod_vec.append(row_res)
	
	return prod_vec