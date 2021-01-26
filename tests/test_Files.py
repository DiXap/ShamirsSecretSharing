# Third-party library imports
import pytest
from unittest import TestCase

# Local library imports
from crypto.Files import FileManager


class FileManager_tests(TestCase):
    """Tests for `FileManager` class"""

    def test_read(self):
        """Reading files test.  
        It's expected for `FileManager.read()` `FileManager.read_shares()` and `FileManager.read_encrypted()` to raise a `FileNotFoundError` if a file doesn't exists
        """
        fm = FileManager()
        with pytest.raises(FileNotFoundError) as error:
            fm.read_shares('core/as')
            fm.read_encrypted('')
            fm.read('test_AESpy')


    def test_write(self):
        """Writing files test.  
        It's expected for `FileManager.write()`, `FileManager.write_shares()` and `FileManager.write_encryption()`to raise a `FileExistsError` if a file already exists and overwriting is not allowed
        """
        fm = FileManager()
        data = 'Data'
        with pytest.raises(FileExistsError) as error:
            fm.write(data, './test_a.py', overwrite= False)
            fm.write_shares(data, './test_a.py', overwrite= False)
            fm.write_encryption(data, './test_a.py', overwrite= False)


    def test_obtain_name(self):
        """Get file name test.  
        It's expected for `FileManager._get_file_name()` to return a file's name without extensions nor complete path
        """
        fm = FileManager()
        file = '/path/to/file/image.jpg.aes'
        file_2 = 'image.jpg.aes'
        file_3 = 'image.aes'
        dummy = 'image'

        real = fm._get_file_name(file)
        real_2 = fm._get_file_name(file_2)
        real_3 = fm._get_file_name(file_3)

        assert real == dummy and real_2 == dummy and real_3 == dummy


    def test_obtain_extension(self):
        """Get file extension test:
        It's expected for `FileManager._get_file_ext()` to return a file's original extension from a encrypted file
        """
        fm = FileManager()
        file = '/path/to/file/main.py.aes'
        file_2 = 'main.py.aes'
        dummy = 'main'

        real = fm._get_file_name(file)
        real_2 = fm._get_file_name(file_2)

        assert real == dummy and real_2 == dummy
