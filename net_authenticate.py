import getpass
import os

import requests

from get_ip import get_host_ip


def net_authenticate():
    file_path = 'login_info.txt'
    flag = True
    if os.path.exists(file_path):
        sz = os.path.getsize(file_path)
        if not sz:
            flag = False
    else:
        flag = False

    if flag:
        with open("login_info.txt", 'r') as file:
            account = file.readline()
            account = account.replace("\n", "")
            password = file.readline()
            password = password.replace("\n", "")
    else:
        with open("login_info.txt", 'w') as file:
            print('请输入学号:')
            account = '__' + input()
            file.write(account + '\n')
            password = getpass.getpass("请输入密码：\n")
            file.write(password + '\n')

    ip = get_host_ip()
    account = account.replace("\n", "")
    password = password.replace("\n", "")
    print(account)
    print(password)
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                      'Safari/537.36',
    }
    data = {
        'DDDDD': account,
        'upass': password,
        'R1': '0',
        'R2': '',
        'R6': '0',
        'para': '00',
        '0MKKey': '123456',
    }

    try:
        print('正在验证...')
        requests.post(
            url='https://portal2.cjlu.edu.cn:801/eportal/?c=ACSetting&a=Login&wlanuserip={}&wlanacip=null&wlanacname=&port=&iTermType=1&mac=000000000000&ip={}&redirect=null=attention&jsonp=jsonp&callback=__jp5'.format(
                ip, ip), headers=header, data=data, verify=False)
        print('登陆成功')

        return True

    except requests.exceptions.ProxyError as err:
        print('未连接校园网或已登录')
        print('错误信息', err)
        return False


if __name__ == '__main__':
    net_authenticate()
