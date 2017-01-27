#encoding=utf8

import requests

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print r
# print r.url
# print r.text
# print r.encoding
# print r.content
# print r.json()

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print r
print r.url
print r.text
print r.encoding
print r.content
print r.json()
print r.raw
print r.raw.read(10)

with open('tmp', 'wb') as fd:
    for chunk in r.iter_content(1024):
        fd.write(chunk)