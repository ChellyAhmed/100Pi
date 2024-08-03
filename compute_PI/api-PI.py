import urllib.request
from test_PI import test_PI
import json

pi_api = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=6"

def getPI():
    result = urllib.request.urlopen(pi_api)
    pi = json.load(result)['content']
    test_PI(float(pi)/100000)


getPI()