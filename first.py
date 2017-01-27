#encoding=utf8

import requests

print requests.get('http://www.baidu.com')
print requests.post('http://httpbin.org/post')
print requests.put('http://httpbin.org/put')
print requests.delete('http://httpbin.org/delete')
print requests.head('http://httpbin.org/get')
print requests.options('http://httpbin.org/get')