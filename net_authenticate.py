import getpass
import os

import requests

from get_ip import get_host_ip

import configparser



def net_authenticate():
        cfr = configparser.ConfigParser()
        cfr.read('conf.ini')
        ip = get_host_ip()
        account = cfr.get('user', 'account')
        password = cfr.get('user', 'password')


        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                          'Safari/537.36',
        }
        params = {
            'callback': 'dr1003',
            'user_account': ',0,__' + account,
            'user_password': password,
            'wlan_user_ip': ip,
            'wlan_user_ipv6': '',
            'wlan_user_mac': '000000000000',
            'wlan_ac_ip': '',
            'wlan_ac_name': '',
            'jsVersion': '4.2.1',
            'terminal_type': '1',
            'v': '7420',
            'lang': 'en'
        }

        try:
            print('正在验证...')
            res = requests.post(
                url='https://portal2.cjlu.edu.cn:802/eportal/portal/login', headers=header, params=params)
            print('登陆成功')
            return True

        except requests.exceptions.ConnectionError as err:
            print('未连接校园网或已登录')
            return False


if __name__ == '__main__':
    net_authenticate()
