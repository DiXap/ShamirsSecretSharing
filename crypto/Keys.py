# Third-party library imports
from Crypto.Hash import SHA3_256


class HashKey():
    """ ### HashKey  
    Class to create and handle secure keys using `SHA3_256`
    """

    def __init__(self, key):
        """Create a new `HashKey` object.  
        Args:
         - key : Passphrase to generate a new key
        """
        self.__key = str(key)


    def sha256_bytes(self):
        """Hash `key` and return it's bytes.  
        Returns:
         - `bytes` : Of the hashed key
        """
        sha256 = SHA3_256.new()
        bytes_key = sha256.update(bytes(self.__key, 'utf-8'))

        return bytes_key.digest()


    def sha256_int(self):
        """Hash `key` and return it as an `int` representation.  
        Returns:
         - `int` : Integer representation of the key
        """
        hashed_key = self.sha256_hex()

        return int(hashed_key, base= 16)


    def sha256_hex(self):
        """Hash `key` and return it as a `hexadecimal` number.  
        Returns:
         - `str` : Of `hex` hashed key
        """
        sha256 = SHA3_256.new()
        bytes_key = sha256.update(bytes(self.__key, 'utf-8'))

        return  bytes_key.hexdigest()
