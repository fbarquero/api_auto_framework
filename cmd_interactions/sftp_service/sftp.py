__author__ = 'it'
import paramiko


class Sftp:
    def __init__(self):
        pass

    def send_files(self, files):
        paramiko.util.log_to_file('/tmp/paramiko.log')
        # Open a transport
        host = "10.111.2.184"
        port = 22
        transport = paramiko.Transport((host, port))

        # Auth
        password = "meds22"
        username = "root"
        transport.connect(username=username, password=password)

        # Go!
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload
        filepath = '/home/foo.jpg'
        localpath = '/home/pony.jpg'
        sftp.put(localpath, filepath)

        # Close

        sftp.close()
        transport.close()
