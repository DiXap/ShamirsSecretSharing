
# Third-party library imports
from unittest import TestCase
from Crypto.Hash import SHA3_256

# Local library imports
from crypto.Keys import HashKey


class test_HashKey(TestCase):
    """Tests for `HashKey` class"""

    def test_sha256_bytes(self):
        """Sha256_bytes test.
        Check if `HashKey.sha256_bytes()` is returning a valid `bytes` key
        """
        passphrase = 'passphrase'
        hash_key = HashKey(passphrase)

        dummy = SHA3_256.new()
        dummy.update(bytes(passphrase, 'utf-8'))

        assert dummy.digest() == hash_key.sha256_bytes()


    def test_sha256_int(self):
        """Sha256_int test.
        Check if `HashKey.sha256_int()` is returning a valid `int` key
        """
        passphrase = 'passphrase'
        hash_key = HashKey(passphrase)

        dummy = SHA3_256.new()
        dummy.update(bytes(passphrase, 'utf-8'))
        dummy_hex = dummy.hexdigest()

        assert int(dummy_hex, base= 16) == hash_key.sha256_int()


    def test_sha256_hex(self):
        """Sha256_hex test.
        Check if `HashKey.sha256_hex()` is returning a valid `hexadecimal` key
        """
        passphrase = 'passphrase'
        hash_key = HashKey(passphrase)

        dummy = SHA3_256.new()
        dummy.update(bytes(passphrase, 'utf-8'))

        assert dummy.hexdigest() == hash_key.sha256_hex()


