__author__ = 'it'

from utils import base_test
import time

import unittest

#TODO preguntarle a rodo si cada vez que un proceso de nose arranca crea una nueva instancia de testing o simplemente utiliza la actual e inicia nuevas ejecuciones sin independizar el self.
#@unittest.skip("testing the skip functionality")
class testing(base_test.base_test):
    def test_1(self):
        self.assert_(5 == 4, msg="text test 1")
        '''
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"
        self.assert_(5 == 4, msg="text")
        '''

    def test_2(self):
        self.assert_(5 == 4, msg="text test_2")
        '''
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"
        '''

    def test_3(self):
        self.assert_(5 == 5, msg="text test_3")
        '''
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"
        '''
    def test_4(self):
        self.assert_(5 == 5, msg="test_4")
        '''
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"
        '''

    def test_5(self):
        self.assert_(5 == 5, msg="text test_5")
        '''
        stdin, stdout, stderr = self.ssh_session.exec_command('ps -A x |grep sshd |grep -v grep')
        print stdout.readlines()
        time.sleep(5)
        print "sleeped 10s"
        '''



