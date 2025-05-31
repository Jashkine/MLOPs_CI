# app_test.py
from app import calculate_square

def test_calculate_square():
    assert calculate_square(0) == 0
    assert calculate_square(2) == 4
    assert calculate_square(-3) == 9
    assert calculate_square(1.5) == 2.25

if __name__ == "__main__":
    test_calculate_square()
    print("All tests passed!")
