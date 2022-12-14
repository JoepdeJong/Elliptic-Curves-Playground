import numpy as np

class EllipticCurve():
    def __init__(self, a, b, p = np.inf):
        """
            This class represents an elliptic curve of the form y^2 = x^3 + ax + b

            Parameters
            ----------
            a : int
                The value of a in the equation
            b : int
                The value of b in the equation
            p : int
                The prime number used to define the field

            a and b must be such that 4a^3 + 27b^2 != 0
        """
        self.a = a
        self.b = b
        self.p = p

        if self.is_singular():
            raise ValueError("The function is singular at this point")

    def is_singular(self):
        """
            This function checks if the function is singular. A function is singular if 4a^3 + 27b^2 = 0
        """
        if 4*self.a**3 + 27*self.b**2 == 0:
            return True
        return False
        
    def f(self, x, y):
        """
            This function returns the value of the function at the point (x, y)
        """
        z = y**2 - (x**3 + self.a*x + self.b)
        return z
    
    def y(self, x):
        """
            This function returns the y-coordinates of the points on the curve with the given x-coordinate
        """
        return np.sqrt((x**3 + self.a*x + self.b))

    def add(self, p: tuple, q: tuple):
        """
            This function adds two points on the curve

            Parameters
            ----------
            p : tuple
                The first point on the curve
            q : tuple
                The second point on the curve
        """
        
        # Compute the slope of the line between p and q
        if p[0] == q[0] and p[1] == q[1]:
            # Doubling of points.
            if p[0] == 0:
                return (np.inf, np.inf)
            m = (3*p[0]**2 + self.a)/(2*p[1])
        if p[0] == q[0]:
            # Point negation, so the line is vertical. The slope is infinite. return the additive identity (O,O).
            return (np.inf, np.inf)
        if p == (np.inf, np.inf):
            # Point at infinity (O,O) + (x, y) = (x, y)
            return q
        if q == (np.inf, np.inf):
            # Point at infinity (x, y) + (O,O) = (x, y)
            return p
        else:
            # Addition for two distinct points is the negation of the intersection point of the line between p and q and the curve
            m = (q[1] - p[1])/(q[0] - p[0])

        # Compute the x-coordinate of the point r
        x = m**2 - p[0] - q[0]
        # Compute the y-coordinate of the point r
        y = m*(p[0] - x) - p[1]

        # If the x-coordinate is greater than the key size, then we need to reduce it modulo the key size
        if x > self.p:
            x = x % self.p

        return (x, y)

    def multiply(self, p: tuple, k: int):
        pi = p
        for i in range(k):
            pi = self.add(pi, p)
        return pi

    def dot(self, p:tuple, q:tuple, k:int):
        """
            This function performs the dotting operation between two points on the curve.

            Parameters
            ----------
            p : tuple
                The first point on the curve.
            q : tuple
                The second point on the curve. The point is used to determine the initial slope.
            k : int
                The number of times the point p is added to itself.
        """

        for i in range(k):
            q = self.add(q, p)
        return q



