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
    def inverse(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        if rows != cols:
            return None
        det = self.determinant(matrix)
        if det == 0:
            return None
        if rows == 2 and cols == 2:
            return [[matrix[1][1]/det,-matrix[0][1]/det],[-matrix[1][0]/det,matrix[0][0]/det]]
        cofactor_matrix = [[self.determinant([row[:j]+row[j+1:] for row in matrix[:i]+matrix[i+1:]])*(-1)**(i+j) for j in range(cols)] for i in range(rows)]
        adjugate = [[cofactor_matrix[j][i] for j in range(rows)] for i in range(cols)]
        return [[adjugate[i][j]/det for j in range(cols)] for i in range(rows)]
        
