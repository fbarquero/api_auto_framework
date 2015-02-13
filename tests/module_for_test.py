__author__ = 'it'

import time

from utils.base_test import BaseTest
from cmd_interactions.serviced.service.serviced_service import ServiceServiced

import unittest


#@unittest.skip("testing the skip functionality")
class Testing(BaseTest):
    def test_1(self):
        serviced = ServiceServiced(self.ssh_connection)
        print serviced.service_list()


    def test_2(self):
        serviced = ServiceServiced(self.ssh_connection)
        print serviced.service_status()

    def test_3(self):
        self.ssh_connection.run_cmd('ps -A x |grep sshd |grep -v grep', 30)
        time.sleep(5)
        print "sleeped 10s"

    def test_4(self):
        self.ssh_connection.run_cmd('ps -A x |grep sshd |grep -v grep', 30)
        time.sleep(5)
        print "sleeped 10s"

    def test_5(self):
        self.ssh_connection.run_cmd('ps -A x |grep sshd |grep -v grep', 30)
        time.sleep(5)
        print "sleeped 10s"

#def suite():
#    """
#    Construct a test suite
#    """
#    test_suite = unittest.TestSuite()
#    test_suite.addTest(unittest.makeSuite(testing))
#    return test_suite

#runner = unittest.TextTestRunner()
#runner.run(suite())





