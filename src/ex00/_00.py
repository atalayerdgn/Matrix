class Solution:
    def __init__(self, matrix1):
        """Initialize the matrix as a flat list for O(N) space complexity."""
        self.row = len(matrix1)
        self.col = len(matrix1[0])
        self.matrix1 = [elem for row in matrix1 for elem in row]

    def validate_dimensions(self, matrix):
        """Ensure dimensions are consistent with the original matrix."""
        if len(matrix) != self.row or len(matrix[0]) != self.col:
            raise ValueError("Matrices must have the same dimensions")

    def flatten(self, matrix):
        """Flatten a 2D matrix into a 1D list."""
        return [elem for row in matrix for elem in row]

    def reshape(self):
        """Reshape the flat list back into a 2D matrix."""
        return [self.matrix1[i * self.col:(i + 1) * self.col] for i in range(self.row)]

    def _add(self, matrix):
        """Add another matrix to the current matrix in O(N) time."""
        self.validate_dimensions(matrix)
        flat_matrix = self.flatten(matrix)
        for i in range(len(self.matrix1)):
            self.matrix1[i] += flat_matrix[i]

    def _sub(self, matrix):
        """Subtract another matrix from the current matrix in O(N) time."""
        self.validate_dimensions(matrix)
        flat_matrix = self.flatten(matrix)
        for i in range(len(self.matrix1)):
            self.matrix1[i] -= flat_matrix[i]

    def scl(self, value):
        """Scale the matrix by a constant value in O(N) time."""
        for i in range(len(self.matrix1)):
            self.matrix1[i] *= value
