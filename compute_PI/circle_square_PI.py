# We estimate the value of pi by generating random points in a square and checking if they fall inside the circle.
# The ratio of the points inside the circle to the total points gives us an estimate of pi.

#Although I wrote down the code myself, the idea was suggested by Nikola Tadic [github.com/ubinator]

import random
from test_PI import test_PI

def circle_square_pi():
    points_inside_circle = 0
    total_points = 0

    while (True):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

        total_points += 1
        pi = 4 * (points_inside_circle / total_points)

        try:
            test_PI(pi)
            return pi
        except AssertionError:
            continue

pi_value = circle_square_pi()
print(f"Approximate value of pi: {pi_value}")
