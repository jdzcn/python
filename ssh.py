#!/usr/bin/python3

import paramiko

def ssh_client():
    # 创建一个实例化
    ssh = paramiko.SSHClient()
    # 加载系统HostKeys密钥
    ssh.load_system_host_keys()
    # 自动添加策略，保存远端主机的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接，默认拒接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #连接远端主机
    ssh.connect('172.96.193.223',port=28147, username='root', password='')
    #执行命令
    stdin, stdout,stderr = ssh.exec_command('tail -10 /var/log/apache2/access.log')
    print(stdout.read().decode('utf-8'))
    #关闭连接
    ssh.close()

if __name__ == '__main__':
    ssh_client()
