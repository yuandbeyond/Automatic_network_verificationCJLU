import os
import getpass
import time

from ping import ping


def vpn_authenticate():
    file_path = 'vpn_info.txt'
    print('正在连接网络')

    flag = True
    if os.path.exists(file_path):
        sz = os.path.getsize(file_path)
        if not sz:
            flag = False
    else:
        flag = False

    if flag:
        with open("vpn_info.txt", 'r') as file:
            name = file.readline()
            name = name.replace("\n", "")
            user_name = file.readline()
            user_name = user_name.replace("\n", "")
            user_psw = file.readline()
            user_psw = user_psw.replace("\n", "")
    else:
        with open("vpn_info.txt", 'w') as file:
            print('请输入VPN服务器名称:')
            name = input()
            file.write(name + '\n')

            print('请输入服务器用户名:')
            user_name = input()
            file.write(user_name + '\n')

            user_psw = getpass.getpass("请输入服务器连接密码：\n")
            file.write(user_psw + '\n')

    os.system('rasdial {} {} {}'.format(name, user_name, user_psw))
    if ping('http://www.baidu.com')==200:
        print('连接成功，程序将在3后自动关闭')
        time.sleep(3)
    else:
        print('连接失败')


if __name__ == '__main__':
    vpn_authenticate()
