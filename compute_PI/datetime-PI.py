import time
from datetime import datetime, timedelta
from test_PI import test_PI


def datetimePI():
    seconds = 365 * 24 * 60 * 60  # Seconds passing in a year
    milliseconds = 996  # We want to get milliseconds of a year when we know the end result will be smaller than PI
    step = 0.000001  # then increase the milliseconds in very small steps
    while True:
        try:
            current_day_in_seconds = time.time()
            epoch_time_a_year_ago = (datetime.today() - timedelta(milliseconds=seconds * milliseconds)).timestamp()
            pi = (current_day_in_seconds - epoch_time_a_year_ago) / 10000000
            test_PI(pi)
            print('Found PI from date %s' % datetime.fromtimestamp(epoch_time_a_year_ago).isoformat())
            return pi
        except AssertionError:
            milliseconds = milliseconds + step


print(datetimePI())
