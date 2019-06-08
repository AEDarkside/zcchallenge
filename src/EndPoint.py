import json
import requests
from settings import subdomain, api_user, api_pwd, list_url #settings.py is store on local machine only during development
from utils import connectToApi

class EndPoint:
    def __init__(self, subdomain):
        self._subdomain = subdomain

    #Request Ticket via HTTP request (experimental)
    def TicketListing(self):
        target_url = subdomain + list_url
        response = connectToApi(self, target_url)
        data = response.json()
        ticket_count = data['count']
        #check if response code other than 200
        if response.status_code != 200:
            print('Request Error, Status code: ', response.status_code)
            exit()
        else:
            print('Request Successful, Status code: ', response.status_code)
            if ticket_count > 25:
                pages = int(ticket_count / 25)
                remamin_tkts = ticket_count - pages * 25
                curr_page = 1
                while pages > 0: 
                    for i in range((curr_page-1) * 25, curr_page * 25):
                        print(data['tickets'][i]['id'])
                    curr_page += 1
                    pages -= 1

            if data['next_page'] != 'null':
                next_page = data['next_page']
                response = connectToApi(self, next_page)
                data = response.json()
                #check if response code other than 200
                if response.status_code != 200:
                    print('Request Error, Status code: ', response.status_code)
                    exit()
                else:
                    if remamin_tkts > 25:
                        pages = int(remamin_tkts / 25)
                        curr_page = 1
                        while pages > 0: 
                            for i in range((curr_page-1) * 25, curr_page * 25):
                                print(data['tickets'][i]['id'])
                            curr_page += 1
                        pages -= 1
                    else:
                        for i in range(0, remamin_tkts):
                            print(data['tickets'][i]['id'])

view_ticket = EndPoint(subdomain)
view_ticket.TicketListing()