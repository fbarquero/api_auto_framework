__author__ = 'fbarquero'

#url = http://segfault.in/2010/03/paramiko-ssh-and-sftp-with-python/

#notes:
# nose get result in teardown:
# http://stackoverflow.com/questions/14077299/how-to-make-nose-to-log-output-of-cases-to-separate-files
# http://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method/4415062#4415062
import unittest
from nose.core import TextTestResult
from connection.ssh_connect import SshConnection


class BaseTest(unittest.TestCase):
    _multiprocess_can_split_ = True
    textTestRunner = TextTestResult()
    #_multiprocess_shared_ = True

    # def setUp(self):
    #
    #     pass

    def tearDown(self):
        print 'algo'
        print self.textTestRunner.wasSuccessful()
