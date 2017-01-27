# encoding=utf8

import requests

url = 'http://httpbin.org/post'
files= {'file': open('tmp', 'rb')}

r = requests.post(url, files=files)
r.text
