import configparser
import os

from net_authenticate import net_authenticate
from vpn_authenticate import vpn_authenticate


def check():
    cfr = configparser.ConfigParser()
    cfr.read('conf.ini')
    for section in cfr.sections():
        for option in cfr.options(section):
            if cfr.get(section, option) == '':
                return False
    return True


if __name__ == '__main__':
    if not os.path.isfile("conf.ini"):
        print('请在同一目录下的conf.ini文件中完成登录信息后再次运行')
        with open('conf.ini', 'w') as f:
            cfr = configparser.ConfigParser()
            cfr.read('conf.ini')
            cfr.add_section('user')
            cfr.add_section('vpn')
            cfr.set('user', 'account', '')
            cfr.set('user', 'password', '')
            cfr.set('vpn', 'name', '')
            cfr.set('vpn', 'username', '')
            cfr.set('vpn', 'password', '')
            cfr.write(f)
    else:
        if check():
            if net_authenticate():
                vpn_authenticate()
            else:
                os.system('pause')

        else:
            print('请在同一目录下的conf.ini文件中完成登录信息后再次运行')
