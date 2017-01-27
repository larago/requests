#encoding=utf8

import requests

r = requests.get('http://httpbin.org/get')
print r.status_code
print requests.codes.ok
print requests.codes.ok == r.status_code
print r.raise_for_status()

bad_r = requests.get('http://httpbin.org/status/404')
print bad_r.status_code
bad_r.raise_for_status()