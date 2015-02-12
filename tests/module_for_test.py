import _multiprocessing

__author__ = 'it'
from utils import base_test
import unittest
import time
from nose.plugins.multiprocess import MultiProcess
#@unittest.skip("testing the skip functionality")
class testing(base_test.base_test):
    #to allow the test of this module to be distributed alogn the running processes of Nose
    _multiprocess_shared_ = True
    def test_1(self):
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"

    def test_2(self):
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"

    def test_3(self):
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"

    def test_4(self):
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"

    def test_5(self):
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
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





