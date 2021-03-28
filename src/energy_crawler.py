import requests
from constants import *

def request_data():
    return requests.get(ONS_URL).json()