from test_PI import test_PI


def wallisPI():
    i = 2
    approximation = 1.0
    while True:
        try:
            approximation *= (i / (i - 1)) * (i / (i + 1))
            pi = approximation * 2
            test_PI(pi)
            print('PI FOUND AFTER %d ITERATIONS' % (i / 2))
            break
        except AssertionError:
            i += 2


wallisPI()
