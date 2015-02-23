__author__ = 'fbarquero'

from ui_requests.ui_requests_actions import UiRequestAction
from utils.framework_configs import GlobalConstants as GC


class ServicedHosts:
    def __init__(self):
        pass

    def serviced_host_list(self):
        pass

    def serviced_host_list_ui(self, timestamp):
        payload = dict(time=timestamp)
        r = self.session.get("%s%s" % (GC.CC_URL, '/hosts'), params=payload)
        return r.text

    def serviced_host_remove(self):
        pass

    def serviced_host_add(self):
        pass

    def serviced_host_help(self):
        pass