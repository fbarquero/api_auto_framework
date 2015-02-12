__author__ = 'it'

from utils import base_test
import time

import unittest

#TODO preguntarle a rodo si cada vez que un proceso de nose arranca crea una nueva instancia de testing o simplemente utiliza la actual e inicia nuevas ejecuciones sin independizar el self.
#@unittest.skip("testing the skip functionality")
class testing(base_test.base_test):
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

def suite():
    """
    Construct a test suite
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testing))
    return test_suite

runner = unittest.TextTestRunner()
runner.run(suite())





