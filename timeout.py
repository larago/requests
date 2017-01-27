#encoding=utf8

import requests

r = requests.get('http://github.com', timeout=0.001)
r.raise_for_status()