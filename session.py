# encoding=utf8

import requests

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

# r = s.get('http://httpbin.org/cookies')

# print r.text

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})