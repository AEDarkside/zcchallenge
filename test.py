#This file contain few happy path test
import unittest
from lib.settings import list_url, subdomain, error_code
from lib.utils import (connect_to_Api, connection_error_handling, 
connect_api_with_user_input)

class viewer_test(unittest.TestCase):
    def test_connect_to_api(self):
        target_url = subdomain + list_url
        response = connect_to_Api(self, target_url)
        self.assertEqual(response.status_code, 200)
    
    def test_response_from_api(self):
        target_url = subdomain + list_url
        response = connect_to_Api(self, target_url)
        self.assertTrue(response != None)
    
    def test_fail_auth_request(self):
        target_url = subdomain + list_url
        response = connect_api_with_user_input(self, target_url, 'example', '1234')
        expectError = connection_error_handling(self, response.status_code)
        self.assertTrue(expectError, error_code['401'])

if __name__ == '__main__':
    unittest.main()