class Solution:
    def __init__(self):
        pass
    def determinant(self,matrix):
        cols = len(matrix[0])
        rows = len(matrix)
        if rows != cols:
            return None
        if rows == 2 and cols == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        det = 0
        for col in range(cols):
            submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
            det += matrix[0][col]*self.determinant(submatrix)*(-1)**col
        return det

    
