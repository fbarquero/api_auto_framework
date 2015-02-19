from nose.tools import timed

__author__ = 'fbarquero'

import time

from utils.base_test import BaseTest
from cmd_interactions.serviced.service.serviced_service import ServicedService

import unittest


#@unittest.skip("testing the skip functionality")
class Testing(BaseTest):
    def test_1(self):
        # print 'algo'
        # time.sleep(5)
        # print 'sleep 5'
        serviced = ServicedService()
        print serviced.service_list()
        time.sleep(6)
        print "sleeped 10s"
        self.assertEqual(1,2,msg="fallo porque 1 no es igual a 2")


    # def test_2(self):
    #     # print 'algo'
    #     # time.sleep(5)
    #     # print 'sleep 5'
    #     serviced = ServicedService()
    #     print serviced.service_list()
    #     time.sleep(6)
    #     print "sleeped 10s"
    #     # serviced = ServiceServiced(self.ssh_connection)
    #     # print serviced.service_status()
    #
    # def test_3(self):
    #     # print 'algo'
    #     time.sleep(6)
    #     # print 'sleep 5'
    #
    #     serviced = ServicedService()
    #     print serviced.service_status()
    #     time.sleep(6)
    #     print "sleeped 10s"
    #
    # def test_4(self):
    #     # print 'algo'
    #     # time.sleep(5)
    #     # print 'sleep 5'
    #
    #     serviced = ServicedService()
    #     print serviced.service_status()
    #     time.sleep(6)
    #     print "sleeped 10s"
    #
    # def test_5(self):
    #     # print 'algo'
    #     # time.sleep(5)
    #     # print 'sleep 5'
    #     time.sleep(6)
    #     print "sleeped 10s"

#def suite():
#    """
#    Construct a test suite
#    """
#    test_suite = unittest.TestSuite()
#    test_suite.addTest(unittest.makeSuite(testing))
#    return test_suite

#runner = unittest.TextTestRunner()
#runner.run(suite())





