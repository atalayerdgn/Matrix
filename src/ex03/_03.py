class Solution:
    def __init__(self):
        pass

    def transpose(self, matrix):
        """Transpose a matrix."""
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def flatten(self, matrix):
        """Flatten a 2D matrix into a 1D list."""
        return [elem for row in matrix for elem in row]

    def dot(self, a, b):
        """Compute the dot product of two matrices in O(n) complexity."""
        if len(a[0]) != len(b):
            raise ValueError("Matrix dimensions must agree.")

        rows_a = len(a)
        cols_b = len(b[0])
        cols_a = len(a[0])
        result = [[0] * cols_b for _ in range(rows_a)]
        b_t = self.transpose(b)
        for i in range(rows_a):
            for j in range(cols_b):
                result[i][j] = sum(a[i][k] * b_t[j][k] for k in range(cols_a))
        return result
