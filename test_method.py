from unittest import TestCase
import requests

class TestTornadoRequest(TestCase):
    base_url = ' http://localhost:9000'
    def test_get(self):
        url = self.base_url + '/'
        resp = requests.get(url, params={
            'wd': "diswn",
            "title": "xian"
        })
        print(resp.text)
    def test_index_post(self):
        url = self.base_url + '/'
        resp = requests.post(url ,data = {
            'data':"diswn",
            "city":"xian"
        })
        print(resp.text)

    def test_index_put(self):
        url = self.base_url + '/'
        resp = requests.put(url ,data = {
            'form1':"diswn",
            # 可以有冗餘參數，但不能缺少參數
            "city":"xian"
        })
        print(resp.text)