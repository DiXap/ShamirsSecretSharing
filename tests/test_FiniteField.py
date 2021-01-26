
# Third-party library imports
import pytest
from unittest import TestCase

# Local library imports
from maths.FiniteField import FiniteField


class test_FiniteField(TestCase):
    """Tests for `FiniteField` class"""

    def test_init(self):
        """Initialize test.  
        It's expected for `FiniteField.__init__()` to throw an exception if its prime is zero
        """
        with pytest.raises(ValueError) as error:
            ff = FiniteField(0)
