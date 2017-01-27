from contextlib import closing
import requests

with closing(requests.get('http://www.baidu.com', stream=True)) as r:
    print r.headers.get('Server')