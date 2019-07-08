import getpass
import threading

"""
"""

import base64
import hashlib
import hmac
import json
import re
import time
from http import cookiejar
from urllib.parse import urlencode
import requests


class zhihu_account(object):
    def __init__(self, username: str = None, password: str = None):
        self.username = username
        self.password = password
        self.login_data = {
            'client_id': 'c3cef7c66a1843f8b3a9e6a1e3160e20',
            'grant_type': 'password',
            'source': 'com.zhihu.web',
            'username': '',
            'password': '',
            'lang': 'en',
            'ref_source': 'homepage',
            'utm_source': ''
        }
        self.session = requests.session()
        self.session.headers = {
            'accept-encoding': 'gzip, deflate, br',
            'Host': 'www.zhihu.com',
            'Referer': 'https://www.zhihu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        self.session.cookies = cookiejar.LWPCookieJar(filename='./cookies.txt')
