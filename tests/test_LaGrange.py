# Standard library imports
import random, functools

# Third-party library imports
import numpy.polynomial.polynomial as polynomial
from unittest import TestCase
from numpy.polynomial.polynomial import Polynomial

# Local library imports
from maths.LaGrange import LaGrange
from crypto.Keys import HashKey


class LaGrange_tests(TestCase):
    """Tests for `LaGrange` class"""

    def test_lagrage_random_polynomial(self):
        """LaGrange polynomial test.  
        Varify correct operations of `LaGrange.random_polynomial()`
        """
        lagrange = LaGrange()
        k = random.randint(2, 100)

        key = HashKey('passphrase')

        poly = Polynomial(lagrange.random_polynomial(key.sha256_int(), k))

        assert poly.degree() == k-1


    def test_lagrange_zero(self):
        """LaGrange polynomial zero test.  
        Check Lagrange polynomial interpolation at 0
        """
        lagrange = LaGrange()
        k = random.randint(2, 10)
        n = random.randint(11, 30)
        key = HashKey('passphrase')
        poly = Polynomial(lagrange.random_polynomial(key.sha256_int(), k))
        random_number = functools.partial(random.SystemRandom().randint, 0)

        x_points = []
        for _ in range(1, n + 1):
            x_points.append(random_number(lagrange.field.get_prime() - 1))
        shares = [
            (x_points[i], lagrange.field.equivalence(polynomial.polyval(x_points[i], poly.coef) ))
            for i in range(len(x_points))
        ]

        assert key.sha256_int() == lagrange.lagrange_zero(shares, 0)
