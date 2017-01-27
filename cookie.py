# encoding=utf8

import requests

url = 'http://www.baidu.com'
r = requests.get(url)

print r.cookies

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
print "cookies' value is ", cookies
r = requests.get(url, cookies=cookies)
print 'down below is text of reponse'
print r.text