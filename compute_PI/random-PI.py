from test_PI import test_PI
import random

def random_PI():
    try:
        hopefullyPi = random.uniform(3.1, 3.2)
        test_PI(hopefullyPi)
        print("Finally pi!")
        return hopefullyPi
    except AssertionError:
        print("Not pi")
        return random_PI()
    
random_PI()
