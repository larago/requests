# encoding=utf8

import requests

r = requests.get('http://github.com')
print r.url
print r.status_code
print r.history

# allow redirection

r = requests.get('http://github.com', allow_redirects=False)
print r.url
print r.status_code
print r.history

# set allow_recirects to True
r = requests.get('http://github.com', allow_redirects=True)
print r.url
print r.status_code
print r.history

r = requests.head('http://github.com', allow_redirects=True)
print r.url
print r.history