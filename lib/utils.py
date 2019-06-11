import requests, base64, datetime, sys, os
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
def print_ticket_list(self, response, curr_page):
    data = response.json()
    ticket_count = data['count']
    print('Request Successful, Status code: ', response.status_code)
    pages = int(ticket_count / int(ticket_limit))
    remamin_tkts = ticket_count - pages * int(ticket_limit)

    #display total pages
    if(remamin_tkts > 0):
        pages += 1
    print('page number: ' + str(curr_page) + ' of ' + str(pages) + ' page(s).'
    + '\n' + 100 * '-')
    #print title for each page
    title_str = ''
    for item in data['tickets'][0]:
       if item in list_item:
            title_str += str(list_item[str(item)])
    print(title_str)

    #print ticket
    for ticket in data['tickets']:
        for item in ticket:
            if item in list_item:
                if item == 'created_at':
                    date_obj = datetime.datetime.strptime(str(ticket[str(item)]), "%Y-%m-%dT%H:%M:%SZ")
                    create_date = date_obj.strftime(time_format)
                elif item == 'id':
                    ticket_id = str(ticket[str(item)])
                elif item == 'status':
                    status = str(ticket[str(item)])
                elif item == 'subject':
                    subject = str(ticket[str(item)])
                elif item == 'requester_id':
                    requester = str(ticket[str(item)])
        print('{:6}'.format(ticket_id)
        + '{:22}'.format(create_date)
        + '{:49.49}'.format(subject)
        + '{:10}'.format(status)
        + '{:15}'.format(requester))

    ticket_list_pagination(self, data['next_page'], data['previous_page'], curr_page)
    
#check if current page has next page or previous page
def ticket_list_pagination(self, next_page, previous_page, curr_page):
    print(100 * '=')

    if (next_page != None) & (previous_page != None):
        choice = input('Press "n" for next page, Press "p" for previous page, or press any key back to menu: ')
        if choice == 'n':
            target_url = next_page
            curr_page += 1
            print_ticket_list(self, connect_to_api(self, target_url), curr_page)
        elif choice == 'p':
            target_url = previous_page
            curr_page -= 1
            print_ticket_list(self, connect_to_api(self, target_url), curr_page)
        else:
            return None 
    elif (next_page != None) & (previous_page == None):
        choice = input('Press "n" for next page, or press any key back to menu: ')
        if choice == 'n':
            target_url = next_page
            curr_page += 1
            print_ticket_list(self, connect_to_api(self, target_url), curr_page)
        else:
            return None
    else:
        choice = input('Press "p" for previous page, or any key back to menu: ')
        if choice == 'p':
            target_url = previous_page
            curr_page -= 1
            print_ticket_list(self, connect_to_api(self, target_url), curr_page)
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
    for item in data['ticket']:
        if item in ticekt_item:
            if item == 'created_at':
                date_obj = datetime.datetime.strptime(data['ticket'][str(item)], "%Y-%m-%dT%H:%M:%SZ")
                create_date = date_obj.strftime(time_format)
            elif item == 'id':
                ticket_id = str(data['ticket'][str(item)])
            elif item == 'status':
                status = str(data['ticket'][str(item)])
            elif item == 'subject':
                subject = str(data['ticket'][str(item)])
            elif item == 'requester_id':
                requester = str(data['ticket'][str(item)])
            elif item == 'description':
                ticket_desc = str(data['ticket'][str(item)])
            elif item == 'priority': 
                priority = str(data['ticket'][str(item)])

    print('{:6}'.format(ticket_id)
    + '{:22}'.format(create_date)
    + '{:49.49}'.format(subject)
    + '{:11}'.format(priority)
    + '{:10}'.format(status)
    + '{:15}'.format(requester))
    print(100 * '-' + '\nTicket Description:\n' + 100 * '-' + '\n' + ticket_desc)

#this is to clear the screen
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

#print main menu
def print_menu():
    print(35 * '=' + 'Welcome to your Ticket Viewer!' + 35 * '='
    + '\nPress 1 - To List all Tickets'
    + '\nPress 2 - To View a Ticket by Ticket ID'
    + '\nType "quit" or Press "q" to exit the program'
    + '\n' + 100 * '-') 

#set terminal size for better user experience when run in windows family
def set_terminal_size():
    if os.name == 'nt':
        os.system("mode con cols=120 lines=50")
        