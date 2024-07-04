from test_PI import test_PI

def increment():
    PI = 0
    while True:
        try:
            PI += 0.00001
            test_PI(PI)
            return PI
        except AssertionError:
            continue

increment()