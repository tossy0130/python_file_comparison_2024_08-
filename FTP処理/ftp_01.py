from ftplib import FTP_TLS

ENCODING = 'utf8'

config = {
    'host': '192.168.254.204',
    'user': 'root',
    'passwd': 'password',
}

with FTP_TLS() as ftp:
    ftp.encoding = ENCODING
    ftp.connect(config['host'])
    ftp.login(config['user'], config['passwd'])
    with open('sample.txt', 'wb') as fp:
        ftp.retrbinary('RETR sample.txt', fp.write)
