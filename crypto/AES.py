# Third-party library imports
from Crypto.Cipher import AES as aes
from Crypto.Hash import SHA3_256


class AES():
    """### AES  
    Class to handle all AES encryption-related methods
    """

    def encrypt(self, key, data):
        """Encrypt data using `AES` scheme following `EAX mode`.  
        Args:
         - key (`bytes`): Hash of a key used to encrypt the data
         - data : Data to encrypt

        Return:
         - `list` : Containing `nonce`, `cipher_tag` and `encrypted_object`
        """
        cipher = aes.new(key, aes.MODE_EAX)
        nonce = cipher.nonce
        encrypted_object, cipher_tag = cipher.encrypt_and_digest(data)

        return [nonce, cipher_tag, encrypted_object]


    def decrypt(self, key, encrypted_data, nonce, tag):
        """Decrypt data using `AES` scheme following `EAX mode`.  
        Validates decryption of the encrypted object.  
        Args:
         - key (`bytes`): Hash of a key to access data
         - encrypted_data : Data to decrypt
         - nonce : Nonce
         - tag : Cipher tag

        Returns:
         - unencrypted_object : 
            - unencrypted_object : upon decryption confirmation
            - `None` : if data is corrupted
        """
        cipher = aes.new(key, aes.MODE_EAX, nonce)
        unencrypted_object = cipher.decrypt(encrypted_data)

        if self._validate_decryption(cipher, tag):
            return unencrypted_object
        else:
            return None


    def _validate_decryption(self, cipher, tag):
        """Auxiliar method to check correct decryption.  
        Args:
         - cipher : AES cipher object
         - tag : Cipher_tag obtained from encrypted data

        Returns:
         - `bool`:
             - `True` : If can varify decryption
             - `False` : If data is corrupted
        """
        try:
            cipher.verify(tag)
            return True
        except ValueError:
            return False
