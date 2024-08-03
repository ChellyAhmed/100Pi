import urllib.request
from test_PI import test_PI
import json

pi_api = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=6"


def getPI():
    result = urllib.request.urlopen(pi_api)
    pi = float(json.load(result)['content']) / 100000
    test_PI(pi)
    return pi


getPI()
