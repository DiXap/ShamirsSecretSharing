# Standard library imports
import pathlib, os

# Local library imports
from .AES import AES


class FileManager():
    """ ### FileManager  
    Class to handle all file `writing`/`reading`.
    """


    def _file_existance(self, file):
        """Auxiliar function to verify file existance.  
        Args:
         - file (`str`) : Path to the file to be verified
        Returns:
         - `bool`:
             - `True` : If it exists
             - `False` : If it doesn't exists
        """
        if pathlib.Path(file):
            return True
        else:
            return False



    def _validate_overwrite(self, file_name, overwrite):
        """Auxiliar function to verify if overwriting a file is possible.  
        Args: 
         - file_name (`str`) : Path to the file to verify
         - overwrite (`bool`) : Overwrite confirmation

        Returns:
         - `bool`:
             - `True` : If overwriting is possible
             - `False` : If overwriting isn't possible
        """
        return (not self._file_existance(file_name)) or overwrite


    def read(self, file):
        """Checks for file existance and reads its content.  
        Args:
         - file (`str`) : Path to the file to read

        Returns:
         - data (`bytes`): File content

        Raises:
         - `FileNotFoundError` : If file doesn't exists
        """
        if self._file_existance(file):
            with open(file, 'rb') as buffer:
                data = buffer.read()
            return data
        else:
            raise FileNotFoundError()


    def read_encrypted(self, encrypted_file):
        """Checks for encrypted file existance and read its content.  
        Args: 
         - encrypted_file (`str`) : Path to the encrypted file to be read

        Returns:
         - `list` : Containing `nonce`, `tag` and `encrypted_data` so it can be easily decrypted by `AES` module

        Raises:
         - `FileNotFoundError` : If file doesn't exists
        """
        if self._file_existance(encrypted_file):
            with open(encrypted_file, 'rb') as buffer:
                nonce, tag = buffer.read(16), buffer.read(16)
                encrypted_data = buffer.read()
            return [nonce, tag, encrypted_data]
        else:
            raise FileNotFoundError()


    def read_shares(self, file):
        """Checks for file existance and reads `Shamir` shares.  
        Args:
         - file (`str`) : Path to the file containing shares

        Returns:
         - shares (`list`) : Of `tuples` containing shares so they can be easily processed

        Raises:
         - `FileNotFoundError` : If file doesn't exists
        """
        if self._file_existance(file):
            with open(file, 'r') as buffer:
                shares = [tuple(map(int, pair.split(','))) for pair in buffer ]
            return shares
        else:
            raise FileNotFoundError()


    def write(self, data, file_name, overwrite= True):
        """Writes a file checking for its existance and overwriting privilege.  
        Args:
         - data : To write
         - file_name (`str`) : Path for the file
         - overwrite (`bool`, optional) : Enable overwriting

        Raises:
         - `FileExistsError` : If file exists and `overwrite` isn't enabled
        """
        if self._validate_overwrite(file_name, overwrite):
            valid_name = self._get_file_name(file_name)
            ext = self._get_file_ext(file_name)

            with open(valid_name + ext, 'wb') as buffer:
                buffer.write(data)
        else:
            raise FileExistsError('File already exists')


    def write_encryption(self, data, nonce, tag, file_name, overwrite= True):
        """Writes `bytes` of encrypted data into a new `.aes` file.  
        Keeps extension of the original file as part of the new name.  
        Args: 
         - data : Encrypted data
         - nonce : Nonce
         - tag : Tag
         - file_name (`str`): Path for the file
         - overwrite (`bool`, optional) : Enable overwriting

        Raises:
         - `FileExistsError` : If file exists and `overwrite` isn't enabled

        """
        if self._validate_overwrite(file_name, overwrite):
            valid_name = self._get_file_name(file_name)
            ext = self._get_file_ext(file_name)
            with open(valid_name + ext + '.aes', 'wb') as buffer:
                buffer.write(nonce)
                buffer.write(tag)
                buffer.write(data)
        else:
            raise FileExistsError()


    def write_shares(self, shares, file_name, overwrite= True):
        """Writes `Shamir`'s shares separating values by comma and tuples by line.  
        Args:
         - shares (`list`) : List of `tuples`
         - file_name (`str`) : Path for the file
         - overwrite (`bool`, optional) : Enable overwriting 

        Raises:
         - `FileExistsError` : If file exists and `overwrite` isn't enabled

        """
        if self._validate_overwrite(file_name, overwrite):
            with open(file_name, 'w') as buffer:
                for (x, y) in shares:
                    tuples = str(x) + ',' + str(y) + '\n'
                    buffer.write(tuples)
        else:
            raise FileExistsError()


    def _get_file_name(self, file_name):
        """Auxiliar function to obtain file's name without extension.  
        Args:
         - file_name (`str`) : File's name

        Returns:
         - name (`str`) : File's name without extension

        """
        if '/' in file_name:
            encrypt_name = file_name.split('/')
            name = encrypt_name[-1].split('.')
        else:
            encrypt_name = file_name
            name = encrypt_name.split('.')

        return name[0]


    def _get_file_ext(self, file_name):
        """Auxiliar function to obtain file's original extenson.  
        Args:
         - file_name (`str`) : File's name

        Returns:
         - `str` : File's original extension

        """
        file = file_name.split('.')

        if len(file) <= 2:
            return '.' + file[-1]
        else:
            return '.' + file[1]


    def remove_file(self, file_name):
        """Check existance of a file, then deletes it.  
        Args:
         -  file_name (`str`) : File's path

        Raises:
         - `FileNotFoundError` : If file doesn't exists

        """
        if self._file_existance(file_name):
            os.remove(file_name)
        else:
            raise FileNotFoundError()
