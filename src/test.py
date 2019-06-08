#This file contain few happy path test
import unittest
from settings import list_url, subdomain
from utils import connectToApi

class ViewerTest(unittest.TestCase):
    def test_connect_to_api(self):
        target_url = subdomain + list_url
        response = connectToApi(self, target_url)
        self.assertEqual(response.status_code, 200)
    
    def test_response_from_api(self):
        target_url = subdomain + list_url
        response = connectToApi(self, target_url)
        self.assertTrue(response != None)

if __name__ == '__main__':
    unittest.main()