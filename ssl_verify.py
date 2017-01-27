#encoding=utf8

import requests

r = requests.get('http://www.baidu.com', verify=True)
print r
