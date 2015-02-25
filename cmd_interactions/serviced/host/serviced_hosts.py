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
        with UiRequestAction() as _session:
            r = _session.get("%s%s" % (GC.CC_URL, '/hosts'), payload)
        return r

    def serviced_host_remove(self):
        pass

    def serviced_host_add(self):
        pass

    def serviced_host_help(self):
        pass