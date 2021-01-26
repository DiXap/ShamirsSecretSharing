# Third-party library imports
from unittest import TestCase

# Test subject import
from crypto.AES import AES


class AES_tests(TestCase):
    """Tests for `AES` class"""

    def test_encrypt(self):
        """Ecryption test.  
        AES.encrypt() is expected to always return something
        """
        dummy = AES()

        passphrase = "ajhskdjbslkjdbas"
        key = str.encode(passphrase)

        data = b'This is a test message to test this test'

        encrypted = dummy.encrypt(key, data)

        assert encrypted != None


    def test_decrypt(self):
        """Decryption test.  
        AES.decrypt() is expected to return `None` if decryption fails
        """
        dummy = AES()

        passphrase = "ajhskdjbslkjdbas"
        key = str.encode(passphrase)

        data = b'This is a test message to test this test'
        encrypted = dummy.encrypt(key, data)

        decryption = dummy.decrypt(key, encrypted[2], encrypted[0], encrypted[1])

        assert decryption != None



