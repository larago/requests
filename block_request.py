#encoding=utf8

import requests

def gen():
    yield 'hi'
    yield 'there'

requests.post('http://www.baidu.com', data=gen())