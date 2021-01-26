
import pytest
from unittest import TestCase
# Third-party library imports
from Crypto.Hash import SHA3_256

# Local library imports
from crypto.ShamirSS import Shamir
from maths.LaGrange import LaGrange
from crypto.AES import AES


class Shamir_tests(TestCase):
    """Tests for `Shamir` class"""

    def test_k_greater_than_n(self):
        """Encryption test.  
        It's expected for `Shamir.encrypt()` to raise an exception if minimum no. of evaluations are greater than total number of evaluations
        """
        dummy = Shamir()
        passphrase = 'oaiksjdassada'
        key = str.encode(passphrase)
        data = b'Data'

        with pytest.raises(ValueError) as error:
            dummy.encrypt(data, 4, 6, passphrase)


    def test_decrypt(self):
        """Decryption test.  
        Tests whether decryption via `Shamir.decrypt()` works properly or not
        """
        shamir = Shamir()
        passphrase = 'oaiksjdassada'
        key = str.encode(passphrase)
        data = b'Data'

        encrypt, shares = shamir.encrypt(data, 10, 7, key)

        dummy = self._decrypt(encrypt, shares)
        real = shamir.decrypt(encrypt, shares)

        assert real == dummy


    def test_reconstruct_polynomial(self):
        """Reconstruct polynomial test.  
        It's expected for `Shamir.reconstruct_polynomial()` to work the same way as `LaGrange.lagrange_zero()` does
        """
        lagrange = LaGrange()
        shamir = Shamir()
        shares = [(165165165161516511,165165165161516511), (165165165161516511,165165165161516511), (165165165161516511,165165165161516511)]

        dummy = lagrange.lagrange_zero(shares, 1)
        real = shamir.reconstruct_polynomial(shares, 1)

        assert real == dummy


    def _decrypt(self, encrypted_data, shares):
        """Auxiliar function that decrypts data without using `Shamir.decrypt()` """
        lagrange = LaGrange()
        aes = AES()
        secret = lagrange.lagrange_zero(shares, 0)

        ki = SHA3_256.new()
        ki.update(bytes(str(secret), 'utf-8'))
        data = aes.decrypt(ki.digest(), encrypted_data[2], encrypted_data[0],encrypted_data[1])

        return data

