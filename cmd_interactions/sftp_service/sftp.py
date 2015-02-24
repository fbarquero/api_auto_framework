__author__ = 'fbarquero'
import paramiko
import ntpath

from utils.framework_configs import GlobalConstants as GC


class Sftp:
    def __init__(self):
        self.sftp = None
        self.transport = None

    def __enter__(self):
        paramiko.util.log_to_file(GC.SFTP_LOG)
        transport = paramiko.Transport((GC.HOSTNAME, GC.SFTP_PORT))
        self.transport.connect(username=GC.USERNAME, password=GC.PASSWORD)
        self.sftp = paramiko.SFTPClient.from_transport(transport)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sftp.close()
        self.transport.close()

    def send_files(self, files, destination_path):
        for filepath in files:
            final_destination_path="%s%s" % (destination_path, self.path_leaf(filepath))
            self.sftp.put(file, final_destination_path)

    def get_files(self, remote_files, destination_path):
        # Download
        for filepath in remote_files:
            final_destination_path="%s%s" % (destination_path, self.path_leaf(filepath))
            self.sftp.get(filepath, final_destination_path)

    def path_leaf(self, file_path):
        head, tail = ntpath.split(file_path)
        return tail or ntpath.basename(head)



# with Sftp() as _sftp_conn:
#     _sftp_conn.get_files(remote_files=['/tmp/a.txt','/tmp/b.txt'], destination_path='c:/temp')
