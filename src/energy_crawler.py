import requests
from constants import *

def request_data():
    
    print(" >> consultando dados da ONS...")

    return requests.get(ONS_URL).json()