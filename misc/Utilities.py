# Standard library imports
import time, sys, os, platform


class UIMisc:
    """### UIMisc  
    Class to complement `ShamirsSecretSharing` UI
    """

    @staticmethod
    def loading(message):
        """Display a progress bar animation with a custom `message`.  

        Args:
         - message (`str`) : Message to be displayed alongside progress bar

        """
        animation = ["[■□□□□□□□□□□□□]", "[■■□□□□□□□□□□□]", "[■■■□□□□□□□□□□]", 
                     "[■■■■□□□□□□□□□]", "[■■■■■□□□□□□□□]", "[■■■■■■□□□□□□□]", 
                     "[■■■■■■■□□□□□□]", "[■■■■■■■■□□□□□]", "[■■■■■■■■■□□□□]", 
                     "[■■■■■■■■■■□□□]", "[■■■■■■■■■■■□□]", "[■■■■■■■■■■■■□]", 
                     "[■■■■■■■■■■■■■]"]

        print('\n' + message)

        for i in range(len(animation)):
            time.sleep(0.01)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()


    @staticmethod
    def success_fail(success= True):
        """Display a `success`/`fail` message.  

        Args:
         - success (`bool`, optional) : Decide which message to display

        """
        ok = [
                    "\n",
                    "\t ============ All green ===========",
                    "\n"
                 ]

        not_ok = [
                    "\n",
                    "\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                    "\t !!!! Something went wrong ... !!!!",
                    "\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                    "\n"
                 ]

        if success:
            for string in ok:
                print(string)
        else:
            for string in not_ok:
                print(string)


    @staticmethod
    def ShamirHeader():
        """Display an ASCII art for `ShamirsSecretSharing`
        """
        header = [
                    "\n",
                    r"  ________  ___  ___  ________  _____ ______   ___  ________          ________   ________       ",
                    r" |\   ____\|\  \|\  \|\   __  \|\   _ \  _   \|\  \|\   __  \        |\   ____\ |\   ____\      ",
                    r" \ \  \___|\ \  \\\  \ \  \|\  \ \  \\\__\ \  \ \  \ \  \|\  \       \ \  \___|_\ \  \___|_     ",
                    r"  \ \_____  \ \   __  \ \   __  \ \  \\|__| \  \ \  \ \   _  _\       \ \_____  \\ \_____  \    ",
                    r"   \|____|\  \ \  \ \  \ \  \ \  \ \  \    \ \  \ \  \ \  \\  \|       \|____|\  \\|____|\  \   ",
                    r"     ____\_\  \ \__\ \__\ \__\ \__\ \__\    \ \__\ \__\ \__\\ _\         ____\_\  \ ____\_\  \  ",
                    r"    |\_________\|__|\|__|\|__|\|__|\|__|     \|__|\|__|\|__|\|__|       |\_________\\_________\ ",
                    r"    \|_________|                                                        \|_________\|_________| ",
                    r"                                                                                                "
                 ]

        for string in header:
            print(string)


    @staticmethod
    def shamir_help():
        """Display `help` menu
        """
        usage = "\n" + "Usage:" + "\n\t" + "python main.py <command> [command's args]\n"
        commands = [
                    "Commands:",
                    "   -c               Encrypt a file.",
                    "   -d               Decrypt a file.",
                    "   -h, --help       Show help."
                    "\n",
                    "Command Args:",
                    "   -c:",
                    "       [<shares' destination file>, <n>, <k>, <file to encrypt>]",
                    "   -d:",
                    "       [<file to decrypt>, <file with shares>]",
                    "\n"
        ]

        UIMisc.ShamirHeader()
        print(usage)
        for item in commands:
            print(item)


    @staticmethod
    def wait_clear(wait_for= 1):
        """Wait for specified period of time and then `clear` terminal.  
        Args:
         - wait_for (`int`, optional) : Seconds to wait for

        """
        time.sleep(wait_for)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


    @staticmethod
    def missing_args():
        """Display an `error` message
        """
        erro = [
                "\n",
                "\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                "\t !!!!!! Somethig went wrong !!!!!!!",
                "\t !!!!!! perhaps missing args !!!!!!",
                "\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                "\n"
        ]

        for string in erro:
            print(string)
