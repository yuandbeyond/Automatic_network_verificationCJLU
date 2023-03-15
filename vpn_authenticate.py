import configparser
import os
import getpass
import time

from ping import ping


def vpn_authenticate():
            cfr = configparser.ConfigParser()
            cfr.read('conf.ini')

            name = cfr.get('vpn','name')
            user_name = cfr.get('vpn','username')
            user_psw = cfr.get('vpn','password')


            os.system('rasdial {} {} {}'.format(name, user_name, user_psw))
            if ping('http://www.baidu.com')==200:
                print('连接成功，程序将在3后自动关闭')
                time.sleep(3)
            else:
                print('连接失败')


if __name__ == '__main__':
    vpn_authenticate()
