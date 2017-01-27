# encoding=utf8

import requests

with open('tmp', 'rb') as f:
    requests.post('http://www.baidu.com', data=f)