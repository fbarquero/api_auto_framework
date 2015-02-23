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

    def get_hosts_in_ui(self, timestamp):
        payload = dict(time=timestamp)
        r = self.session.get("%s%s" % (GC.CC_URL, '/hosts'), params=payload)
        return r.text

# with UiRequestAction as r:
#     r.get_hosts_in_ui()
# # uiRequest=UiRequestAction()
# # uiRequest.get_hosts_in_ui()
#
#

