# Zcchallenge
This is a simple ticket viewer program written in python in response to '**Zendesk Coding Challenge 2019**'


## Ticket Viewer
This Ticket Viewer is a program written in python that will connected to Zendesk API and listing all the tickets on prefilled Zendesk account or view ticket individually.
- When listing all the tickets, if more than 25 tickets returned the program will allow user to page through the list eigther by press 'n' for next page or 'p' for previous page and press any other key will bring the user back to main menu. The list is ordered by ticket id, order from highest to lowest(newest ticket come first).
- Display individual ticket detail by enter a ticket id as the search target

## File Structure
    root\
        lib\
            __init__.py     - empty but author name
            settings.py     - contain secrets, configs and python dictionary
            utils.py        - useful function to call API and parse data into message
        __init__.py         - empty but author name
        end_point.py        - main class contain menu and initialization of the program
        README.md           - readme
        test.py             - contain few tests

## Installation
Python version: 3.6.7, package required: 'request'

- To install python 3.6.7

For Windows:

        1. Go to https://www.python.org/downloads/
        2. Follow the link for the Windows installer python-XYZ.msi file where XYZ is the version you need to install.
        3. save the installer to your machine
        4. run the downloaded file

For Unix and Linux Installation

        1. Go to https://www.python.org/downloads/
        2. Follow the link to download zipped source code for unix/linux
        3. Extract downloaded files
        4. run ./configure script
        5. make
        6. make install

For Macintosh:

        1. See https://www.python.org/download/mac/ for instructions

- To install package 'request' use:

        pip install request

## Setting up PATH variables
- For Windows:

1. In Command prompt(cmd) - type the following and press enter:

        %path%;C:\Python - assume python is installed on C: and C:\Python is
        the path of Python directory


- For Unix/Linux:

1. In csh shell - type the following and press enter:

        setenv PATH "$PATH:/usr/local/bin/python"

2. in bash shell - type the following and press enter:

        export PATH="$PATH:/usr/local/bin/python"

3. in the sh or ksh shell - type the following and press enter:

        PATH="$PATH:/usr/local/bin/python"

## Usage
Change your current working directory to root directory:

- To run the program use:

1. In Unix terminal:

        python end_point.py

2. In Windows powershell:
        
        python3 end_point.py

- To run unit tests use:

1. In Unix terminal:

        python -m unittest test

2. In Windows powershell:

        python3 -m unittest test

## Author
ZhiChao Chen - zc.chen0411@gmail.com