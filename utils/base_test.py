__author__ = 'fbarquero'

#url = http://segfault.in/2010/03/paramiko-ssh-and-sftp-with-python/
import unittest

from connection.ssh_connect import SshConnection


class BaseTest(unittest.TestCase):
    _multiprocess_can_split_ = True
    #_multiprocess_shared_ = True

    # def setUp(self):
    #
    #     pass

    # def tearDown(self):
    # check https://pypi.python.org/pypi/nose_xunitmp/0.2