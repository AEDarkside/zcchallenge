#This file contain few happy path test
import unittest, random
from lib.settings import list_url, subdomain, error_code, content_type, api_url
from lib.utils import (connect_to_api, connection_error_handling, 
connect_api_with_user_input)

class api_connection_test(unittest.TestCase):
    def setUp(self):
        self.target_url = subdomain + list_url
        self.response = connect_to_api(self, self.target_url)

    def test_connect_to_api(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_response_from_api(self):
        self.assertTrue(self.response != None)
    
    def test_fail_auth_request(self):
        response = connect_api_with_user_input(self, self.target_url, 'example', '1234')
        expectError = connection_error_handling(self, response.status_code)
        self.assertTrue(expectError, error_code['401'])

class ticket_viewer_test(unittest.TestCase):
    def setUp(self):
        target_url = subdomain + list_url
        self.response = connect_to_api(self, target_url)
        data = self.response.json()
        self.count = data['count']

    def test_list_all_ticket(self):
        self.assertTrue(self.count > 0)
    
    def test_single_ticket(self):
        ticket_id = random.randint(0, self.count)
        target_url = subdomain + api_url + str(ticket_id) + content_type
        response = connect_to_api(self, target_url)
        ticket = response.json()
        result_id = ticket['ticket']['id']
        self.assertEqual(ticket_id, result_id)

if __name__ == '__main__':
    unittest.main()