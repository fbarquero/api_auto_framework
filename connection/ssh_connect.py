__author__ = 'Mordigan'
import paramiko

class ssh_connection:
    def open_connection(self, username, password, hostname, timeout):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password, timeout=timeout)
        #stdin, stdout, stderr = ssh.exec_command('df -h')
        return ssh

    def close_ssh_connection(self, ssh):
        ssh.close()