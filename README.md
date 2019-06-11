# Zcchallenge
This is a simple ticket viewer program written in python in response to 'Zendesk Coding Challenge 2019',


## Ticket Viewer
Ticket Viewer is a python program connected to Zendesk API and requested all tickets on your account or view them individually.
- When listing all the tickets, if more than 25 tickets returned the program will allow user to page through the list eigther by press 'n' for next page or 'p' for previous page and press any other key will bring the user back to main menu. The list is ordered by ticket id, order from highest to lowest(newest ticket come first).
- Display individual ticket detail by enter a ticket id as the search target

## File Structure
    root\__
        lib\
            __init__.py     - empty but author name
            settings.py     - contain secrets, configs and python dictionary
            utils.py        - useful function to call API and parse data into message
        __init__.py         - empty but author name
        end_point.py        - main class contain menu and initialization of the program
        README.md           - readme
        test.py             - contain few tests

## Usage
Placeholder for now

## Author
ZhiChao Chen - zc.chen0411@gmail.com