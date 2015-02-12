__author__ = 'Mordigan'
import paramiko


class SshConnection:
    def __init__(self):
        self.ssh = None

    def open_connection(self, username, password, hostname, timeout):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname, username=username, password=password, timeout=timeout)
        #stdin, stdout, stderr = ssh.exec_command('df -h')
        return self.ssh

    def close_ssh_connection(self, ssh):
        self.ssh.close()