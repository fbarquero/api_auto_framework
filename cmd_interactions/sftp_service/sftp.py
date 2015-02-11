__author__ = 'it'
import paramiko
import ntpath
import os
from connection import ssh_connect

#TODO set user password, paramiko log and host as params in config file
class Sftp:
    def __init__(self):
        pass

    def send_files(self, files, destination_path):
        paramiko.util.log_to_file('paramiko.log')

        # Open a transport
        host = "10.111.2.217"
        port = 22
        transport = paramiko.Transport((host, port))

        # Auth
        password = "meds22"
        username = "root"
        transport.connect(username=username, password=password)

        # Go!
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload
        for filepath in files:
            final_destination_path="%s%s" % (destination_path, self.path_leaf(filepath))
            sftp.put(file, final_destination_path)

        # Close connections
        sftp.close()
        transport.close()

    def get_files(self, remote_files, destination_path):
        paramiko.util.log_to_file('paramiko.log')

        # Open a transport
        host = "10.111.2.214"
        port = 22
        transport = paramiko.Transport((host, port))

        # Auth
        password = "meds22"
        username = "root"
        transport.connect(username=username, password=password)

        # Go!
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Download
        for filepath in remote_files:
            final_destination_path="%s%s" % (destination_path, self.path_leaf(filepath))
            sftp.get(filepath, final_destination_path)

        # Close
        sftp.close()
        transport.close()

    def path_leaf(self, file_path):
        head, tail = ntpath.split(file_path)
        return tail or ntpath.basename(head)


#sftp = Sftp()
#sftp.get_files(["../../utils/service_files/test.txt"], "/tmp/")
#sftp.get_files(["/tmp/test1.sh", "/tmp/test2.sh"], "../../downloads/")


