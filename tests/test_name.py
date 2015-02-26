__author__ = 'fbarquero'

import time

from utils.base_test import BaseTest
from cmd_interactions.serviced.service.serviced_service import ServicedService

import unittest


#@unittest.skip("testing the skip functionality")
class Testing(unittest.TestCase):
    def test_1(self):
        time.sleep(2)
        self.assertTrue(True)

    def test_2(self):
        time.sleep(2)
        self.assertTrue(True)

    def test_3(self):
        time.sleep(2)
        self.assertTrue(False)

    def test_4(self):
        time.sleep(2)
        self.assertTrue(False)

    def test_5(self):
        time.sleep(2)
        1/0
        self.assertTrue(True)

class Testing_2(BaseTest):
    def test_1(self):
        time.sleep(2)
        self.assertTrue(True)

    def test_2(self):
        time.sleep(2)
        self.assertTrue(True)

    def test_3(self):
        time.sleep(2)
        self.assertTrue(False)

    def test_4(self):
        time.sleep(2)
        self.assertTrue(False)

    def test_5(self):
        time.sleep(2)
        1/0
        self.assertTrue(True)

#def suite():
#    """
#    Construct a test suite
#    """
#    test_suite = unittest.TestSuite()
#    test_suite.addTest(unittest.makeSuite(testing))
#    return test_suite

#runner = unittest.TextTestRunner()
#runner.run(suite())





