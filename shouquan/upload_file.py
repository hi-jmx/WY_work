import ftplib
import paramiko
import uuid

class SSHUpload(object):

    def __int__(self, host='192.168.100.3', port=22, username='root', pwd='test'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        u"""
 链接SFTP
        """
        try:
            self.ssh.connect(self.host, username=self.username, password=self.pwd,  port=self.port, timeout= 1)
            self.sftp = self.ssh.open_sftp()
            print
            u"链接成功..."
            return 1
        except Exception as e:
            print
            u"连接失败..%s" % e
            return 0

    def close(self):
        self.sftp.close()
        self.ssh.close()

    def upload(self, local_path, target_path):
        # 连接，上传
        # file_name = self.create_file()
        # sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        self.sftp.put(local_path, target_path)

    def download(self, remote_path, local_path):
        # sftp = paramiko.SFTPClient.from_transport(self.__transport)
        self.sftp.get(remote_path, local_path)

    # def cmd(self, command):
    #     ssh = paramiko.SSHClient()
    #     ssh._transport = self.__transport
    #     # 执行命令
    #     stdin, stdout, stderr = ssh.exec_command(command)
    #     # 获取命令结果
    #     result = stdout.read()
    #     print(str(result, encoding='utf-8'))
    #     return result

# if __name__ == '__main__':
#     ssh = SShUpload()
#     ssh.__int__(host='192.168.1.179', port=22,username='root', pwd='root')
#     res = ssh.connect()
#     print(res)
#     if (1 == res):
#         ssh.cmd("ls")
#         ssh.upload('config.txt','/dev/shm/ks77.py')
#         ssh.download('/dev/shm/ks77.py','kkkk',)
#         ssh.close()
#     else:
#         print("do nothing")

class FTPUpload(object):
    def __int__(self, host='192.168.100.3', port=21, username='', pwd='test'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.ftp = ftplib.FTP(user=username, passwd=pwd)
    def connect(self):
        try:
            self.ftp.connect(host=self.host, port=self.port, timeout=1)
            try:
                self.ftp.login(user=self.username, passwd=self.pwd)
                return 1
            except Exception as err:
                print("服务器连接失败！！！")
                print(err)
                return 0
        except Exception as err:
            print("服务器连接失败！！！")
            print(err)
            return 0

    def close(self):
        self.ftp.quit()

    def upload(self, local_path, target_path):
        with open(local_path, 'rb') as f:
            self.ftp.storbinary('STOR ' + target_path, f)

    def download(self, remote_path, local_path):
        with open(local_path, 'wb') as f:
            self.ftp.retrbinary('RETR ' + remote_path, f.write)

# if __name__ == '__main__':
#     ssh = SSHUpload()
#     ssh.__int__(host='192.168.1.179', port=22, username='root', pwd='root')
#     res = ssh.connect()
#     print(res)
#     if (1 == res):
#         # ssh.cmd("ls")
#         ssh.upload('config.txt','/dev/shm/ks77.py')
#         ssh.download('/dev/shm/ks77.py','kkkk',)
#         ssh.close()
#     else:
#         print("do nothing")

    # ftp = FTPUpload()
    # ftp.__int__(host='192.168.100.26', port=21, username='test', pwd='test')
    # res = ftp.connect()
    # print(res)
    # if (1 == res):
    #     ftp.upload('config.txt','./config.txt')
    #     ftp.download('Clash.for.Windows-0.20.31-win.7z','./123',)
    #     ftp.close()
    # else:
    #     print("do nothing")


