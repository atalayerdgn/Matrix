class Solution:
    def __init__(self, matrix1, matrix2):
        """
        Initialize the matrices and flatten them for efficient computation.

        Args:
            matrix1 (list of list of float): First matrix.
            matrix2 (list of list of float): Second matrix.
        """
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrices must have the same dimensions.")
        
        self.row = len(matrix1)
        self.col = len(matrix1[0])
        self.matrix1 = [elem for row in matrix1 for elem in row]
        self.matrix2 = [elem for row in matrix2 for elem in row]

    def linear_combination(self, alpha, beta):
        """
        Perform a linear combination of the two matrices in O(N) time.

        Args:
            alpha (float): Coefficient for the first matrix.
            beta (float): Coefficient for the second matrix.
        """
        for i in range(len(self.matrix1)):
            self.matrix1[i] = alpha * self.matrix1[i] + beta * self.matrix2[i]

    def reshape(self):
        """
        Reshape the flattened matrix back into its original 2D form.

        Returns:
            list of list of float: Reshaped 2D matrix.
        """
        return [self.matrix1[i * self.col:(i + 1) * self.col] for i in range(self.row)]
