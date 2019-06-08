import requests
from settings import api_user, api_pwd

def connectToApi(self, target_url):
    response = requests.get(target_url, auth=(api_user, api_pwd))
    return response