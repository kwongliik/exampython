# test_calculation.py

from question_1 import calculation

def test_calculation():
    # Test case 1
    result = calculation(40, 10)
    assert result == (30, 400, 4), "Test case 1 failed"

    # Test case 2 (add more as needed)
    result = calculation(20, 5)
    assert result == (15, 100, 4), "Test case 2 failed"
