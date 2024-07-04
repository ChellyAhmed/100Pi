import math

def test_PI(number):
    if isinstance(number, str):
        number = float(number)
    difference = abs(number - math.pi)
    assert difference < 0.0001

def returnPI():
    return 3.14159265
