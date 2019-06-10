import requests, base64
from os import name, system
from lib.settings import api_user, api_pwd, error_code

#decrypt password for use in authentication
def get_password(self, api_pwd):
    return base64.b64decode(api_pwd)

#this function connect to zendesk api taking the url as parameter
def connect_to_Api(self, target_url):
    pwd = get_password(self, api_pwd)
    response = requests.get(target_url, auth=(api_user, pwd))
    return response

#this function for test purpose
def connect_api_with_user_input(self, target_url, user, pwd):
    response = requests.get(target_url, auth=(user, pwd))
    return response

def connection_error_handling(self, status_code):
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

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def print_menu():
    print(35 * '-' + 'Welcome to your Ticket Viewer!' + 35 * '-'
    + '\nPress 1 - Listing all Tickets'
    + '\nPress 2 - View a Ticket by Ticket ID'
    + '\nType "quit" to exit'
    + '\n' + 100 * '-') 