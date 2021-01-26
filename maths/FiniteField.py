# Standard library imports
import random


class FiniteField(object):

    """ ### FiniteField  
    Class that allows to work with finite fields' arithmetic ensuring that all numbers exists under this finite field.
    """

    def __init__(self, prime):
        """ Initialize our `Finitefield` object with a given `prime` number
        """
        if prime != 0:          # Check if prime is different from zero
            self.prime = prime  # Assign it
        else:
            raise ValueError    # Raise an error if prime is negative


    # Following algorithm was obtained from https://stackoverflow.com/questions/17383236/python-multiplicative-inverse-in-gf2-finite-field
    # Modified to suit this project's needs
    def extended_euclides(self, a, b):
        """Apply `Extended Euclidean Algorithm` to obtain `gcd`.  
        Args:
         - a (`int`) : To find gcd with b.
         - b (`int`) : To ind gcd with a.

        Returns:
         - last_x, last_y (`list`) : gcd(a, b) as a list for better value access.
        """
        x = last_y = 0
        y = last_x = 1
        while b != 0:
            quot = a // b
            a, b = b, a % b
            x, last_x = last_x - quot * x, x
            y, last_y = last_y - quot * y, y

        return [last_x, last_y]

    def division(self, num, denom):
        """Perform modular `division` according finite fields' aritmethic.  
        Args:
         - num (`int`) : Numerator
         - denom (`int`) : Denominator

        Returns:
         - `int` : Result thrown by modular division
        """
        inverse = self.extended_euclides(denom, self.prime)[0]  # Apply our extended euclidean algo and obtain the first item of the list, this sould be the inverse
        return num * inverse                                    # Multiply the inverse for the numerator to obtain quotient


    def equivalence(self, n):
        """Obtain equivalence class of a certain number.  
        Args:
         - n (`int`) : Number to obtain equivalence

        Returns:
         - `int` : Equivalence as `n % prime`
        """
        return n % self.prime


    def random_int(self, top):
        """Generate random int `n` such that `0 <= n <= prime`.  
        Args:
         - top (`int`) : Interval limit

        Returns:
         - `int` : Random `int` under this `FiniteField`
        """
        return random.randint(0, top) % self.prime


    def get_prime(self):
        """Obtain this finite fields `prime` number.  
        Returns:
         - `int` : Prime number
        """
        return self.prime
