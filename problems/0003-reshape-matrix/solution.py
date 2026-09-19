def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    # Write your code here and return a python list after reshaping by using numpy's tolist() method
	
	target_row, target_cols = new_shape
    # Flatten original matrix
    flattened = [val for row in a for val in row]

    # Check if total elements match the target shape
    if len(flattened) != target_row * target_cols:
        return []
    
    # Chunk into target_cols per row
    return [
        flattened[i : i + target_cols] 
        for i in range(0, len(flattened), target_cols)
    ]