class Solution:
    def __init__(self):
        pass
    def transpose(self, matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            new_matrix.append([row[i] for row in matrix])
        return new_matrix
