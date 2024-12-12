class Solution:
    def __init__(self):
        pass
    def trace(self, matrix):
        """Calculate the trace of a square matrix."""
        result = 0
        for i in range(len(matrix)):
            result += matrix[i][i]
        return result
