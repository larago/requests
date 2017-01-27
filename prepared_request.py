#encoding=utf8

from requests import Request, Session

s = Session()

url='http://www.baidu.com'
data=''
headers=''

req = Request('GET', url,
    data=data,
    headers=headers)
prepared = req.prepare()

# do something with prepared.body
# do something with prepared.headers
prepared.body = 'ok'
prepared.headers={'key':'val'}
print prepared.url
print prepared.body
print prepared.headers

resp = s.send(prepared,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout)

print resp.status_code