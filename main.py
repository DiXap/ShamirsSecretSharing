# Standard library imports
import sys

# Local library imports
from core.ArgsParser import CryptoParser
from misc.Utilities import UIMisc


if __name__ == '__main__':
    main = CryptoParser(sys.argv)
    try:
        main.run()
    except Exception:
        UIMisc.missing_args()

