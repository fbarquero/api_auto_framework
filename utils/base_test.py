__author__ = 'Mordigan'

#url = http://segfault.in/2010/03/paramiko-ssh-and-sftp-with-python/
import unittest

from connection.ssh_connect import SshConnection


class BaseTest(unittest.TestCase):
    _multiprocess_can_split_ = True
    #_multiprocess_shared_ = True

    # def setUp(self):
    #     pass
    #
    # def tearDown(self):
    #     #TODO add try exept
    #     pass
    #     # try:
    #     #     self.ssh_connection.close_ssh_connection()
    #     # except Exception:
    #     #     pass

