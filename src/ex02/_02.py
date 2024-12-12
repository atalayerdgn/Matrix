class Solution:
    def __init__(self):
        pass
    def lerp(self, a, b, t):
        """Linearly interpolate between two vectors."""
        if len(a) != len(b):
            raise ValueError("Vectors must have the same dimensions.")
        return [[a[i] + t * (b[i] - a[i])] for i in range(len(a))]
