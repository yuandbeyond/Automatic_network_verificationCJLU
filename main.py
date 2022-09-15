import os

from net_authenticate import net_authenticate
from vpn_authenticate import vpn_authenticate

if __name__ == '__main__':
    if net_authenticate():
        vpn_authenticate()
    else:
        os.system('pause')
