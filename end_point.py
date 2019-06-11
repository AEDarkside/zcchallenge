import json, requests
from lib.settings import (subdomain, list_url, api_url, content_type, per_page, 
ticket_limit)
from lib.utils import (connect_to_api, connection_error_handling, clear_screen, 
print_menu, print_ticket_list, print_single_ticket)

class end_point:
    def __init__(self, subdomain):
        self._subdomain = subdomain

    #Request Ticket via HTTP request (experimental)
    def ticket_listing(self):
        target_url = self._subdomain + list_url + per_page + ticket_limit
        response = connect_to_api(self, target_url)
        #check if response code other than 200
        if response.status_code != 200:
            print(connection_error_handling(self, response.status_code))
        else:
            curr_page = 1
            print_ticket_list(self, response, curr_page)
            
    #list one particular ticket with the ticket id provide by the user
    def list_single_ticket(self):
        ticket_id = input('Enter the ticket ID you want to see: ')
        target_url = subdomain + api_url + ticket_id + content_type
        response = connect_to_api(self, target_url)
        data = response.json()
        #check if response code other than 200
        if response.status_code != 200:
            print(connection_error_handling(self, response.status_code))
        else:
            print_single_ticket(self, data)
        input(100 * '=' + '\nNow back to Menu, press any key to continue..')    

    #menu display function
    def display_menu(self):
        menu = True
        while menu:
            clear_screen()
            print_menu()
            choice = input('Select your view option: ')
            if choice == '1':
                view_ticket.ticket_listing()
            elif choice == '2':
                view_ticket.list_single_ticket()
            elif choice in ('quit', 'q'):
                menu = False
                print('Thansk for using the ticket viewer.' + 
                '\nTerminating Ticket Viewer program...')
                exit()
            else:
                input('wrong option selected, press any key back to menu')

view_ticket = end_point(subdomain)
view_ticket.display_menu()