class Solution:
    def __init__(self):
        pass
    def cross_product(self, u, v):
        """
        Calculate the cross product of two vectors (supports only 3D vectors).
        u and v should both be lists or arrays of length 3.
        """
        if len(u) != 3 or len(v) != 3:
            raise ValueError("Cross product is only defined for 3D vectors.")
        result = [
            u[1] * v[2] - u[2] * v[1],  # x-component
            u[2] * v[0] - u[0] * v[2],  # y-component
            u[0] * v[1] - u[1] * v[0],  # z-component
        ]
        return result
