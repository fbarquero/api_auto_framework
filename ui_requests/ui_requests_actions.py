__author__ = 'Mordigan'
# http://docs.python-requests.org/en/latest/user/quickstart/
import requests
import json


class UiRequestAction:
    def __init__(self):
        pass


    def authentify(self):
        payload = dict(username='root', password='meds22')
        url = "https://10.111.2.129/login"
        session = requests.Session()
        r = session.post(url, data=json.dumps(payload), verify=False, stream=False)
        print session.headers
        print r.text