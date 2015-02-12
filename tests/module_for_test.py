__author__ = 'it'

from utils import base_test
import time

import unittest


#@unittest.skip("testing the skip functionality")
class testing(base_test.base_test):
    def test_1(self):
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"
        self.assert_(5 == 4, msg="text")


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



