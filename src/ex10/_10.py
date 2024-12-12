class Solution:
    def __init__(self):
        pass

    def is_row_echelon_form(self, matrix):
        cols = len(matrix[0])
        prev = -1
        for row in matrix:
            leading_col = next((col for col in range(cols) if row[col] != 0), cols)
            if leading_col <= prev:
                return False
            if all(elem == 0 for elem in row[leading_col + 1:]):
                prev = leading_col
        return True

    def find_nonzero_row(self, matrix, pivot_row, col):
        rows = len(matrix)
        for row in range(pivot_row, rows):
            if matrix[row][col] != 0:
                return row
        return None

    def swap_rows(self, matrix, row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

    def make_pivot_one(self, matrix, pivot_row, col):
        pivot_element = matrix[pivot_row][col]
        if pivot_element != 0:
            matrix[pivot_row] = [val / pivot_element for val in matrix[pivot_row]]

    def eliminate_below(self, matrix, pivot_row, col):
        nrows = len(matrix)
        for row in range(pivot_row + 1, nrows):
            factor = matrix[row][col]
            if factor != 0:  # Avoid unnecessary calculations
                matrix[row] = [
                    matrix[row][i] - factor * matrix[pivot_row][i]
                    for i in range(len(matrix[0]))
                ]

    def row_echelon_form(self, matrix):
        ncols = len(matrix[0])
        nrows = len(matrix)
        pivot_row = 0
        for col in range(ncols):
            if pivot_row >= nrows:  # Avoid out-of-bound errors
                break
            nonzero_row = self.find_nonzero_row(matrix, pivot_row, col)
            if nonzero_row is not None:
                self.swap_rows(matrix, pivot_row, nonzero_row)
                self.make_pivot_one(matrix, pivot_row, col)
                self.eliminate_below(matrix, pivot_row, col)
                pivot_row += 1
        # Replace all occurrences of -0.0 with 0.0
        matrix = [[0.0 if abs(val) < 1e-10 else val for val in row] for row in matrix]
        return matrix
