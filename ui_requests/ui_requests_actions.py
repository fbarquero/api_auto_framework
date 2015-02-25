__author__ = 'Mordigan'
# http://docs.python-requests.org/en/latest/user/quickstart/
import requests
import json

from utils.framework_configs import GlobalConstants as GC


class UiRequestAction:
    def __init__(self):
        self.session = None

    def __enter__(self):
        payload = dict(username=GC.USERNAME, password=GC.PASSWORD)
        self.session = requests.Session()
        self.session.post("%s%s" % (GC.CC_URL, '/login'), data=json.dumps(payload), verify=False, stream=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def get(self, url, payload):
        r = self.session.get(url, params=payload)
        return r.text



with UiRequestAction() as r:
    json_response = json.loads(r.get("%s%s" % (GC.CC_URL, '/hosts'), payload=dict(time='1424793514')))
    print 'algo'


#
#

