import requests, base64
from settings import api_user, api_pwd, error_code

def getPassword(self, api_pwd):
    return base64.b64decode(api_pwd)

#this function connect to zendesk api taking the url as parameter
def connectToApi(self, target_url):
    pwd = getPassword(self, api_pwd)
    response = requests.get(target_url, auth=(api_user, pwd))
    return response

#this function for test purpose
def connectToApiWithUserInput(self, target_url, user, pwd):
    response = requests.get(target_url, auth=(user, pwd))
    return response

def connectionErrorHandling(self, status_code):
    if status_code == 400:
        return error_code['400']
    elif status_code == 401:
        return error_code['401']
    elif status_code == 403:
        return error_code['403']
    elif status_code == 404:
        return error_code['404']
    elif status_code == 500:
        return error_code['500']
    elif status_code == 502:
        return error_code['502']
    elif status_code == 503:
        return error_code['503']
    elif status_code == 504:
        return error_code['504']    