def add(a: int , b: int) -> int:
    return a + b
def subtract(a: int, b: int) -> int:
    return b - a
def multiply(a: int, b: int) -> int:
    return a * b
def divide(a: int, b: int) -> int:
    return b // a


def test_add() -> int:
    assert add(1, 1) == 11
def test_subtract() -> int:
    assert subtract(2, 5) == 3
def test_multiply() -> int:
    assert multiply(10, 10) == 100
def test_divide() -> int:
    assert divide(25, 100) == 4