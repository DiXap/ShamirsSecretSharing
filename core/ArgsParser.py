# Standard library imports 
import sys, getpass

# Third-party library imports
from crypto.ShamirSS import Shamir
from crypto.Files import FileManager

# Local library imports
from misc.Utilities import UIMisc as UI

class CryptoParser():

    """ ### CryptoParser 
    Custom `argsparser` class to create a UI for `ShamirsSecretSharing`
    """

    def __init__(self, args):
        """Initialize `CryptoParser` with system `args`
        """
        self.args = args
        self.ui = UI()


    def run(self):
        """Start `CryptoParser`
        """
        if self.args:
            files_manager = FileManager()

            if self.args[1] == '-c' and len(self.args) == 6:                                                            # Encrypt
                shares_destination, n, k, to_ecrypt = self.args[2], self.args[3], self.args[4], self.args[5]
                shamir = Shamir()

                try:
                    silent_passphrase = self.silet_parser('Enter a passphrase: ')
                    data = files_manager.read(to_ecrypt)
                    encrypted_data, shares = shamir.encrypt(data, int(n), int(k), silent_passphrase)

                    files_manager.write_encryption(encrypted_data[2], encrypted_data[0], encrypted_data[1], to_ecrypt)
                    files_manager.write_shares(shares, shares_destination)

                    self.ui.loading('Encrypting ...')
                    self.ui.wait_clear(wait_for= 0.9)

                    files_manager.remove_file(to_ecrypt)
                    self.ui.ShamirHeader()
                    self.ui.success_fail()

                except Exception:
                    self.ui.success_fail(success= False)
                    self.ui.wait_clear(wait_for= 2)

                finally:
                    sys.exit(1)

            if self.args[1] == '-d' and len(self.args) == 4:                                                            # Decrypt
                to_decrypt, shares_file = self.args[2], self.args[3]
                shamir = Shamir()

                try:
                    shares = files_manager.read_shares(shares_file)
                    encrypted_data = files_manager.read_encrypted(to_decrypt)
                    unencrypted = shamir.decrypt(encrypted_data, shares)
                    files_manager.write(unencrypted, to_decrypt)

                    self.ui.loading('Decrypting ...')
                    self.ui.wait_clear(wait_for= 0.8)

                    files_manager.remove_file(to_decrypt)
                    self.ui.ShamirHeader()
                    self.ui.success_fail()

                except Exception:
                    self.ui.success_fail(success= False)
                    self.ui.wait_clear(wait_for= 2)

                finally:
                    sys.exit(1)

            if self.args[1] == '-h' or self.args[1] == '--help':                                                        # Display help
                self.ui.shamir_help()

            else:
                self.ui.ShamirHeader()
                self.ui.success_fail(success= False)
        else:
            raise Exception()


    def silet_parser(self, message):
        """Recieve user input without echoing to terminal.  
        Args:
         - message (`str`) : Custom message to prompt
        """
        return getpass.getpass(message)
