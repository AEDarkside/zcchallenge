import json
import requests
from src.settings import subdomain, list_url, api_url, content_type, per_page, ticket_limit #settings.py is store on local machine only during development
from src.utils import connectToApi, connectionErrorHandling, print_menu, clear_screen

class EndPoint:
    def __init__(self, subdomain):
        self._subdomain = subdomain

    #Request Ticket via HTTP request (experimental)
    def TicketListing(self):
        target_url = self._subdomain + list_url + per_page + ticket_limit
        response = connectToApi(self, target_url)
        #check if response code other than 200
        if response.status_code != 200:
            print(connectionErrorHandling(self, response.status_code))
        else:
            data = response.json()
            ticket_count = data['count']
            clear_screen()
            print('Request Successful, Status code: ', response.status_code)
            pages = int(ticket_count / int(ticket_limit))
            remamin_tkts = ticket_count - pages * int(ticket_limit)
            if(remamin_tkts > 0):
                pages += 1
            print('You have total of ' + str(pages) + ' pages of tickets' 
            + '\n' + 100 * '-')
            for ticket in data['tickets']:
                print(ticket)
            if (data['next_page'] != None) & (data['previous_page'] != None):
                choice = input('Press "n" for next page, Press "p" for previous page: ')
            elif (data['next_page'] != None) & (data['previous_page'] == None):
                choice = input('Press "n" for next page: ')
            else:
                choice = input('Press "p" for previous page: ')

            
    #list one particular ticket with the ticket id provide by the user
    def list_single_ticket(self):
        ticket_id = input('Enter the ticket ID you want to see: ')
        target_url = subdomain + api_url + ticket_id + content_type
        response = connectToApi(self, target_url)
        data = response.json()
        if response.status_code != 200:
            print(connectionErrorHandling(self, response.status_code))
        else:
            for item in data['ticket']:
                print(str(item) + ': ', data['ticket'][str(item)])
        input(100 * '-' + '\nNow back to Menu, press any key to continue..')    

    #menu display function
    def display_menu(self):
        menu = True
        while menu:
            print_menu()
            choice = input('Select your view option: ')
            if choice == '1':
                view_ticket.TicketListing()
            elif choice == '2':
                view_ticket.list_single_ticket()
            elif choice in ('quit', 'q'):
                menu = False
                print('Closing down Ticket Viewer...')
                exit()
            else:
                input('wrong option selected, press any key back to menu')

view_ticket = EndPoint(subdomain)
view_ticket.display_menu()