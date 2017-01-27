#encoding=utf8

import requests

r = requests.get('http://httpbin.org/get')
print r.status_code