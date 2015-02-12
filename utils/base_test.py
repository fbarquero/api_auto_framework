from paramiko.ssh_gss import _SSH_GSSAPI

__author__ = 'Mordigan'

# url = http://segfault.in/2010/03/paramiko-ssh-and-sftp-with-python/
import unittest
from connection import ssh_connect


class base_test(unittest.TestCase):
    _multiprocess_can_split_ = True

    def setUp(self):
        self._ssh_connection = ssh_connect.SshConnection()
        self.ssh_session = self._ssh_connection.open_connection('root', 'meds22', '10.111.2.214', 30)


    def tearDown(self):
        self._ssh_connection.close_ssh_connection(self.ssh_session)