class Solution:
    def __init__(self):
        pass
    def magnitude(self, u):
        """Calculate the magnitude of a vector."""
        return sum(u_i ** 2 for u_i in u) ** 0.5
    def dot(self, u, v):
        """Compute the dot product of two matrices in O(n) complexity."""
        return sum(u_i * v_i for u_i, v_i in zip(u, v))
    def cosine_angle(self, a, b):
        """Compute the cosine similarity of two vectors."""
        if len(a) != len(b):
            raise ValueError("Vectors must have the same dimensions.")
        a_dot_b = self.dot(a, b)
        mag = self.magnitude(a) * self.magnitude(b)
        return a_dot_b / mag
