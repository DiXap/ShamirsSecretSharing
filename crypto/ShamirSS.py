# Standard library imports
import functools, random

# Third-party library imports
from Crypto.Hash import SHA3_256
from numpy.polynomial.polynomial import Polynomial
import numpy.polynomial.polynomial as polynomial

# Local library imports
from .AES import AES
from .Keys import HashKey
from maths import LaGrange


class Shamir():

    """ ### Shamir  
    Class in charge of executing `Shamir's Secret Sharing` algorithm. 
    """

    def __init__(self):
        """Create a `Shamir` object.
        With all necessary atributes to perform correctly
        """
        self._aes = AES()                                                          #  Handles AES file encryption
        self._lagrange = LaGrange.LaGrange()                                       #  In charge of all mathematical calculations
        self._random_number = functools.partial(random.SystemRandom().randint, 0)  #  Generates random integers under a finite field


    def encrypt(self, data, n, k, passphrase):
        """Encrypt data using `Shamir's SS` and `AES` scheme.  
        Args:
         - data : Data to encrypt.
         - n (`int`) : Total evaluations to be done.
         - k (`int`) : Minimum evaluations requiered to `decrypt`.
         - passphrase (`str`) : Passphrase to secure `encryption`.

        Returns:
         - encrypted_data, shares (`data`, `list`): As a `tuple` containing encrypted data and all `shares`

        """
        if n < k or k == 1:           # If number of total evals is greater than minimum no. of evals raise an Error
            raise ValueError()

        ki = SHA3_256.new()           # Create an object to hash according to SHA-3 256
        key = HashKey(passphrase)     # Hash the passphrase with our own HashKey class
        s = str(key.sha256_int())     # Hash and convert to integer so we can operate with it, then cast to a string
        ki.update(bytes(s, 'utf-8'))  # Update ki with the resulting string to prepare it to hash so we can use it to encrypt with AES

        poly = Polynomial(self._lagrange.random_polynomial(key.sha256_int(), k))        #  Create a Polynomial object based on our own LaGrange polynomial

        x_points = []                                                                   #  Create an empty list
        for _ in range(1, n + 1):
            x_points.append(self._random_number(self._lagrange.field.get_prime() - 1))  #  Generate numbers under our finite field to evaluate the polynomial

        # Evaluate the polynomial and populate a list with tuples containing (x, P(x)) a.k.a our list of shares
        shares = [
            (x_points[i], self._lagrange.field.equivalence(polynomial.polyval(x_points[i], poly.coef) ))
            for i in range(len(x_points))
        ]

        encrypted_data = self._aes.encrypt(ki.digest(), data)  # Encrypt our data with AES 

        return (encrypted_data, shares)


    def reconstruct_polynomial(self, shares, x):
        """ Reconstruct the polynomial for `Shamir's SS`.  
        Args:
         - shares (`list`) : A list of `tuples` containing polynomial evaluations `(x, P(x))`.
         - x (`int`) : Term to find.

        Returns:
         - evals (`int`) : Result of the Interpolation

        """
        evals = self._lagrange.lagrange_zero(shares, x)  # Use our LaGrange method to reconstruct polynomial

        return evals


    def decrypt(self, encrypted_data, shares):
        """Decrypt data using `Shamir's SS` and `AES` scheme.  
        Args:
         - encrypted_data : Data to decrypt
         - shares (`list`) : List of tuples containing polynomial evaluations `(x, P(x))` a.k.a `shares`

        Returns:
         - data : Unencrypted data

        """
        secret = self.reconstruct_polynomial(shares, 0)                                                 # Reconstruct polynomial with given shares

        ki = SHA3_256.new()                                                                             # Create an object to hash according to SHA-3 256
        ki.update(bytes(str(secret), 'utf-8'))                                                          # Update ki object so it's ready to re-hash

        data = self._aes.decrypt(ki.digest(), encrypted_data[2], encrypted_data[0], encrypted_data[1])  # Decrypt data

        return data

