class Solution:
    def __init__(self):
        pass
    def flatten(self, matrix):
        """Flatten a 2D matrix into a 1D list."""
        return [elem for row in matrix for elem in row]
    def norm_1(self, x):
        """Calculate the L1 norm of a matrix."""
        resul = 0
        new = self.flatten(x)
        for i in new:
            resul += abs(new[i])
        return resul
    def norm_2(self, x):
        """Calculate the L2 norm of a matrix."""
        result = 0
        new = self.flatten(x)
        for i in new:
            result += abs(new[i])**2
        return result**(1/2)
    def norm_inf(self, x):
        """Calculate the L-infinity norm of a matrix."""
        result = 0
        new = self.flatten(x)
        for i in new:
            if abs(new[i]) > result:
                result = abs(new[i])
        return result
        
