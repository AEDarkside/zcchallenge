import requests, base64, datetime
from os import name, system
from lib.settings import (api_user, api_pwd, error_code, list_item, time_format, 
ticket_limit, ticekt_item)

#decrypt password for use in authentication
def get_password(self, api_pwd):
    return base64.b64decode(api_pwd)

#this function connect to zendesk api taking the url as parameter
def connect_to_api(self, target_url):
    pwd = get_password(self, api_pwd)
    response = requests.get(target_url, auth=(api_user, pwd))
    return response

#this function for test purpose
def connect_api_with_user_input(self, target_url, user, pwd):
    response = requests.get(target_url, auth=(user, pwd))
    return response

#return corresponding error message base on status_code
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

#print all tickets in a list
def print_ticket_list(self, response):
    data = response.json()
    ticket_count = data['count']
    print('Request Successful, Status code: ', response.status_code)
    pages = int(ticket_count / int(ticket_limit))
    remamin_tkts = ticket_count - pages * int(ticket_limit)
    #display total pages
    if(remamin_tkts > 0):
        pages += 1
    print('You have total of ' + str(pages) + ' pages of tickets' 
    + '\n' + 100 * '-')
    #print title for each page
    title_str = ''
    for item in data['tickets'][0]:
       if item in list_item:
            title_str += str(list_item[str(item)])
    print(title_str)    
    #print ticket
    for ticket in data['tickets']:
        ticket_str = ''
        for item in ticket:
            if item in list_item:
                if item == 'created_at':
                    date_obj = datetime.datetime.strptime(str(ticket[str(item)]), "%Y-%m-%dT%H:%M:%SZ")
                    ticket_str += date_obj.strftime(time_format) + '    '
                else: 
                    ticket_str += str(ticket[str(item)]) + '    '
        print(ticket_str)
    #check if it contain next page or previous page
    if (data['next_page'] != None) & (data['previous_page'] != None):
        choice = input('Press "n" for next page, Press "p" for previous page, or press any key back to menu: ')
        if choice == 'n':
            target_url = data['next_page']
            print_ticket_list(self, connect_to_api(self, target_url))
        elif choice == 'p':
            target_url = data['previous_page']
            print_ticket_list(self, connect_to_api(self, target_url))
        else:
            return None 
    elif (data['next_page'] != None) & (data['previous_page'] == None):
        choice = input('Press "n" for next page, or press any key back to menu: ')
        if choice == 'n':
            target_url = data['next_page']
            print_ticket_list(self, connect_to_api(self, target_url))
        else:
            return None
    else:
        choice = input('Press "p" for previous page, or any key back to menu: ')
        if choice == 'p':
            target_url = data['previous_page']
            print_ticket_list(self, connect_to_api(self, target_url))
        else:
            return None

#print ticket by ticket_id
def print_single_ticket(self, data):
    title_str = ''
    for item in data['ticket']:
        if item in ticekt_item:
            if item == 'description':
                continue
            else:
                title_str += str(ticekt_item[str(item)])
    print(title_str)    
    #print ticket
    ticket_str = ''
    for item in data['ticket']:
        if item in ticekt_item:
            if item == 'created_at':
                date_obj = datetime.datetime.strptime(data['ticket'][str(item)], "%Y-%m-%dT%H:%M:%SZ")
                ticket_str += date_obj.strftime(time_format) + '    '
            elif item == 'description':
                ticket_desc = str(data['ticket'][str(item)])
            else: 
                ticket_str += str(data['ticket'][str(item)]) + '    '
    print(ticket_str + '\n' + 
        100 * '-' + '\nDescription: \n' + ticket_desc)

#this is to clear the screen
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#print main menu
def print_menu():
    print(35 * '-' + 'Welcome to your Ticket Viewer!' + 35 * '-'
    + '\nPress 1 - To List all Tickets'
    + '\nPress 2 - To View a Ticket by Ticket ID'
    + '\nType "quit" or Press "q" to exit the program'
    + '\n' + 100 * '-') 