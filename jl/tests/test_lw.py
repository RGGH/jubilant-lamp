"""
test lw multiply function
"""

from lw import multiply

# Run the actual multiply test
def test_multiply():
    """
    Verify 2 * 3 equals 6
    """
    assert multiply(2,3) == 6
