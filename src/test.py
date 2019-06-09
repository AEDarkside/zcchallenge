#This file contain few happy path test
import unittest
from settings import list_url, subdomain, error_code
from utils import connectToApi, connectionErrorHandling, connectToApiWithUserInput

class ViewerTest(unittest.TestCase):
    def test_connect_to_api(self):
        target_url = subdomain + list_url
        response = connectToApi(self, target_url)
        self.assertEqual(response.status_code, 200)
    
    def test_response_from_api(self):
        target_url = subdomain + list_url
        response = connectToApi(self, target_url)
        self.assertTrue(response != None)
    
    def test_fail_auth_request(self):
        target_url = subdomain + list_url
        response = connectToApiWithUserInput(self, target_url, 'example', '1234')
        expectError = connectionErrorHandling(self, response.status_code)
        self.assertTrue(expectError, error_code['401'])

if __name__ == '__main__':
    unittest.main()