#encoding=utf8

import requests

def print_url(r, *args, **kwargs):
    print r.url
hooks = dict(response=print_url)

requests.get('http://www.baidu.com', hooks=hooks)