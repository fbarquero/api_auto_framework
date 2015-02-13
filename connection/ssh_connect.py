__author__ = 'Mordigan'
import paramiko


class SshConnection:
    def __init__(self):
        self.ssh = None

    # def open_connection(self, username, password, hostname, timeout=15):
    #     self.ssh = paramiko.SSHClient()
    #     self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     self.ssh.connect(hostname, username=username, password=password, timeout=timeout)

    def run_cmd(self, command, timeout=15):

        username = 'root'
        password = 'meds22'
        hostname = '10.111.2.214'
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname, username=username, password=password, timeout=timeout)
        # self.open_connection('root', 'meds22', '10.111.2.214', timeout)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        unicode_output = stdout.readlines()
        self.ssh.close()
        return unicode_output