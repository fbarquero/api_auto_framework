__author__ = 'Mordigan'
# http://docs.python-requests.org/en/latest/user/quickstart/
import requests
import json


class UiRequestAction:
    def __init__(self):
        pass

    def authentify(self):
        payload = dict(username='root', password='meds22')
        url = "https://10.111.2.214/login"
        session = requests.Session()
        r = session.post(url, data=json.dumps(payload), verify=False, stream=False)
        print session.headers
        print r.text
        return session

    def get_hosts_in_ui(self):
        session = self.authentify()
        # 1423642201
        url = "https://10.111.2.214/hosts"
        payload = {'time': '1423642201'}
        r = session.get(url, params=payload)
        print session.headers
        print r.text

# uiRequest=UiRequestAction()
# uiRequest.get_hosts_in_ui()



