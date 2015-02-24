__author__ = 'fbarquero'

import time

from utils.base_test import BaseTest
from cmd_interactions.serviced.service.serviced_service import ServicedService



class Testing(BaseTest):
    def test_zenoss_can_start(self):
        """
        Given: Just one Zenoss application was deployed, it is currently on stopped status
        When: User starts Zenoss deployed app
        Then: Zenoss status of all daemons are "Running"
        """
        #Instances section
        serviced = ServicedService()
        #Start Zenoss app
        started = serviced.service_start('Zenoss.resmgr')
        self.assertTrue(msg='Unable to start the service')
        self.assertTrue(serviced.is_zenoss_running(), msg='Zenoss did not started correctly')

    def test_2(self):
        print 'test number 2 intended to fail'
        time.sleep(10)
        self.assertTrue(False, msg='Expected failure on test 2')

    def test_3(self):
        print 'test number 3 intended to fail'
        time.sleep(10)
        self.assertTrue(False, msg='Expected failure on test 3')

    def test_4(self):
        print 'test number 4 intended to PASS'
        time.sleep(10)
        self.assertTrue(True, msg='Expected failure on test 4')

    def test_5(self):
        print 'test number 4 intended to Have an error'
        time.sleep(5)
        divide = 1 / 0
        self.assertTrue(False, msg='Expected failure on test 4')




