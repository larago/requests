# encoding=utf8

import requests

s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print r.text

r = s.get('http://httpbin.org/cookies')
print r.text
requests.utils.add_dict_to_cookiejar(s.cookies, {'cookie1':'val'})
print requests.utils.dict_from_cookiejar(s.cookies)

with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    print requests.utils.dict_from_cookiejar(s.cookies)