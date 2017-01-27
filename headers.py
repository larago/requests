# encoding=utf8

import requests

r = requests.get('http://www.baidu.com')
print r.headers
print r.headers.get('content-encoding', None)