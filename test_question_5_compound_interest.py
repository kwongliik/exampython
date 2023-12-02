# test_compound_interest.py
from question_5_compound_interest import compound_interest

def test_compound_interest():
    assert compound_interest(1000, 5, 2, 1) == 1102.50
    assert compound_interest(1500, 3.5, 3, 4) == 1665.3051756777352
    assert compound_interest(2000, 7, 5, 12) == 2835.2505192279805
