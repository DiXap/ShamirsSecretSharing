# Standard library imports
import functools,random

# Local libray imports
from .FiniteField import FiniteField


class LaGrange():

    """ ### LaGrange  
    Class to correctly handle Lagrange interpolation
    """

    def __init__(self, prime_number= 208351617316091241234326746312124448251235562226470491514186331217050270460481):
        """Initialize `LaGrange` object.
        Args:
         - prime_number (`int`) : 256 bit prime number to initialize a `FiniteField`.
        """
        self.field = FiniteField(prime_number)                                    # Create new field with recived prime_number
        self.random_number = functools.partial(random.SystemRandom().randint, 0)  # Create an object to obtain random numbers
                                                                                  #   turns out that this works better than FiniteField.random_int()


    def lagrange_polynomial(self, i, x, points):
        """Obtain `Li(x)` from Lagrange polynomial interpolation.  
        Args:
         - i (`int`) : `x_i`
         - x (`int`) : Value to be found
         - points (`list`) : Points for the polynomial

        Returns:
         - `int` : Evaluation `Li(x)`
        """
        num = denom = 1                         # Aux to calculate Li(x)

        for j in range(len(points)):            # Iterate over the points
            if points[j] != i:                  # As long as a point doesn't match with x_i proceed with evals
                num *= (x - points[j])          # Evaluate
                denom *= (i - points[j])        # Evaluate

        return self.field.division(num, denom)  # Finally divide to find Li(x)


    def random_polynomial(self, independent_term, k):
        """Generate random polnomial coefficients under self `FiniteField`.  
        Args:
         - independent_term (`int`) : Independent term for the polynomial
         - k (`int`) : Polynomial degree

        Returns:
         - coefficients (`list`) : Containing polynomial coefficients
        """
        coefficients = [self.random_number(self.field.get_prime() - 1) for i in range(k)]  #  Populate a list with random numbers as polynomial coeffs.
        coefficients[0] = independent_term                                                 #  Insert independent term, for Shamir this is gonna be our big-integer hashed key

        return coefficients


    def lagrange_zero(self, shares, x):
        """Reconstruct a Lagrange polynomial using various evaluations a point.  
        Args:
         - shares (`list`) : Containing tuples of `(x, P(y))` points
         - x (`int`) : Term to find

        Returns:
         - `int` : Result of the Interpolation
        """
        result = 0
        x_points, y_points = zip(*shares)                                    # Agroup tuples in two list as [x_n], [P(x_n)] for better data access

        for i in range(len(x_points)):
            polynomial = self.lagrange_polynomial(x_points[i], x, x_points)  # Evaluate every point
            product = self.field.equivalence(polynomial * y_points[i])       # Find its equivalence
            result += product                                                # Keep track of the total

        return self.field.equivalence(result)
