__author__ = 'fbarquero'


class GlobalConstants:
    #Master config info
    HOSTNAME = '10.111.2.112'
    USERNAME = 'root'
    PASSWORD = 'meds22'
    CC_URL = 'https://%s' % HOSTNAME

    #SFTP config info
    SFTP_PORT = 22
    SFTP_LOG = "sftp_conn_log.log"

    #SSH config info
    DEFAULT_TIMEOUT=30

class GlobalMsg:
    ASSERTTRUE_MSG='ESTO ES UN MENSAGE'
