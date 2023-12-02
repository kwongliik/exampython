from question_4_max import max_value

def test_max_value_a():
    assert max_value(30, 22, 18) == 30

def test_max_value_b():
    assert max_value(10, 40, 30) == 40

def test_max_value_c():
    assert max_value(5, 8, 15) == 15

def test_max_value_equal():
    assert max_value(20, 20, 20) == 20

