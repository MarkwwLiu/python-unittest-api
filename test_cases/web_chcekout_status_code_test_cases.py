import unittest
import requests
from config import domain

class WebApiTestCase(unittest.TestCase):

    def test_share_web_check_status_200(self):
        get_requests = requests.get(url=domain.web_domain_dict['share_web'])
        print(domain.web_domain_dict['share_web'])
        print(get_requests)
        self.assertEqual(get_requests.status_code, 200, '返回狀態不為200，請驗證')

    def test_google_web_check_status_200(self):
        get_requests = requests.get(url=domain.web_domain_dict['google_web'])
        print(domain.web_domain_dict['google_web'])
        print(get_requests)
        self.assertEqual(get_requests.status_code, 200, '返回狀態不為200，請驗證')

    def test_yahoo_web_check_status_200(self):
        get_requests = requests.get(url=domain.web_domain_dict['yahoo_web'])
        print(domain.web_domain_dict['yahoo_web'])
        print(get_requests)
        self.assertEqual(get_requests.status_code, 200, '返回狀態不為200，請驗證')
