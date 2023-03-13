from unittest import TestCase
import requests


class CiCd(TestCase):
    def test_run_server(self):
        response = requests.get('http://185.182.111.243/')
        reference = 'Stocks-Products API'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, reference)
