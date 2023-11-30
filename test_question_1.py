# test_calculation.py

from question_1 import calculation

def test_calculation():
    # Test case 1
    result = calculation(40, 10)
    assert result == (50, 30), "Test case 1 failed"

    # Test case 2 (add more as needed)
    result = calculation(20, 5)
    assert result == (25, 15), "Test case 2 failed"
