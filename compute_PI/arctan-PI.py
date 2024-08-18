# arctan(1) = pi/4 . Therefore 4 * arctan(1) = pi
import math
from test_PI import test_PI

def arctanPI():
    pi = 4 * math.atan(1)
    print(pi)
    test_PI(pi)
    return pi
    
arctanPI()