#encoding=utf8

import requests

r = requests.get('http://www.baidu.com')
print "response's header: ", r.headers
print "request's header: ", r.request.headers