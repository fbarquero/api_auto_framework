__author__ = 'Mordigan'
import paramiko


class SshConnection:
    def __init__(self):
        self.ssh=None
    # def __init__(self):
    #     self.ssh = None
    def __enter__(self, timeout=15):
        print 'in enter'
        username = 'root'
        password = 'meds22'
        hostname = '10.111.2.214'
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname, username=username, password=password, timeout=timeout)
        return self

    # def open_connection(self, username, password, hostname, timeout=15):
    #     self.ssh = paramiko.SSHClient()
    #     self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     self.ssh.connect(hostname, username=username, password=password, timeout=timeout)

    def run_cmd(self, command, timeout=15):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        unicode_output = stdout.readlines()
        return unicode_output

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "closing ssh"
        self.ssh.close()