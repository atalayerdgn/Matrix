class Solution(object):
    def __init__(self):
        self.R = 0  # Rows (not defined in the constructor)
        self.C = 0  # Columns (not defined in the constructor)
        
    # Function for exchanging two rows of a matrix
    def swap(self, Matrix, row1, row2, col):
        for i in range(col):
            temp = Matrix[row1][i]
            Matrix[row1][i] = Matrix[row2][i]
            Matrix[row2][i] = temp
            
    # Function to display a matrix
    def Display(self, Matrix, row, col):
        for i in range(row):
            for j in range(col):
                print(" " + str(Matrix[i][j]))
            print('\n')
            
    # Find the rank of a matrix
    def rank(self, Matrix):
        self.R = len(Matrix)  # Update the row count
        self.C = len(Matrix[0])  # Update the column count
        
        rank = self.C
        for row in range(0, self.R, 1):  # Iterate over rows, not columns
            if row >= rank:
                break

            # Ensure mat[row][0], .... mat[row][row-1] are 0.
            if Matrix[row][row] != 0:
                for col in range(0, self.R, 1):
                    if col != row:
                        # This makes all entries of the current column 0
                        multiplier = (Matrix[col][row] /
                                      Matrix[row][row])
                        for i in range(rank):
                            Matrix[col][i] -= (multiplier *
                                               Matrix[row][i])
                                                
            else:
                reduce = True
                
                # Find a non-zero element in the current column
                for i in range(row + 1, self.R, 1):
                    if Matrix[i][row] != 0:
                        self.swap(Matrix, row, i, rank)
                        reduce = False
                        break
                        
                if reduce:
                    # Reduce the number of columns
                    rank -= 1
                    
                    # Copy the last column here
                    for i in range(0, self.R, 1):
                        Matrix[i][row] = Matrix[i][rank]
                        
                # Process this row again
                row -= 1
                
        return rank
