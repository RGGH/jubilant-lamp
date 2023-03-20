import pytest

"""
test lw multiply function
"""

from lw import multiply


# Run the actual multiply test
def test_multiply_success():
    """
    Verify 2 * 3 equals 6
    """
    assert multiply(2,3) == 6

def test_multiply_value_err():
    """
    Verify string input fails
    """
    with pytest.raises(TypeError):
        multiply('two','three')
    