__author__ = 'it'
import paramiko
import ntpath
import os
from connection import ssh_connect


class Sftp:
    def __init__(self):
        pass

    def send_files2(self, files, destination_path, ssh_session):
        paramiko.util.log_to_file('paramiko.log')

        # Open a transport

        host = "10.111.2.217"
        port = 22
        transport = paramiko.Transport((host, port))

        # Auth

        password = "meds22"
        username = "root"
        transport.connect(username = username, password = password)

        # Go!

        sftp = paramiko.SFTPClient.from_transport(transport)

        # Download

        #filepath = '/etc/passwd'
        #localpath = '/home/remotepasswd'
        #sftp.get(filepath, localpath)

        # Upload


        for file in files:
            final_destination_path="%s%s" % (destination_path, self.path_leaf(file))
            sftp.put(file, final_destination_path)

        # Close

        sftp.close()
        transport.close()

    def path_leaf(self, file_path):
        head, tail = ntpath.split(file_path)
        return tail or ntpath.basename(head)


conn = ssh_connect.SshConnection()
ssh_session = conn.open_connection("root", "meds22", "10.111.2.217", 60)
sftp = Sftp()
sftp.send_files2(["../../utils/service_files/test.txt"], "/tmp/", ssh_session)
#file_path = "C:\\Users\Mordigan\\PycharmProjects\\api_auto_framework\\utils\\service_files\\test.txt"
#file = open(file_path, 'r')
#print file.read()
#file.close()
#file2 = open(file_path.replace('\\', '/'), 'r')
#print file2.read()
#file2.close()

