#encoding=utf8

import requests

tarball_url = 'https://www.baidu.com'
r = requests.get(tarball_url, stream=True)

# print r.headers
# if int(r.headers['content-length']) < 1000000:
#     content = r.content
#     print content

# print dir(r)
# for i in r.iter_content:
#     print i
for i in r.iter_lines():
    print i