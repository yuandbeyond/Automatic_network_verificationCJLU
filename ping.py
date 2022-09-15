import requests


def ping(url):
    try:
        res = requests.get(url)
        return res.status_code
    except requests.exceptions.ProxyError as err:
        return err


if __name__ == '__main__':
    ping('https://www.baidu.com')
