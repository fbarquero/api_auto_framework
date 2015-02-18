__author__ = 'fbarquero'
import paramiko

from utils.framework_configs import GlobalConstants as GC

class SshConnection:
    def __init__(self):
        self.ssh=None

    def __enter__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ssh.close()

    def run_cmd(self, command, timeout=GC.DEFAULT_TIMEOUT):
        self.ssh.connect(GC.HOSTNAME, username=GC.USERNAME, password=GC.PASSWORD, timeout=timeout)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        unicode_output = stdout.readlines()
        return unicode_output
