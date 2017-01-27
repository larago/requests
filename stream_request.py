#encoding=utf8

import requests
import json

r = requests.get('http://httpbin.org/stream/20', stream=True)

# total = 0
# for line in r.iter_lines():
#     if line:
#         total += 1
#         print json.loads(line)
# print total

# store it if you access over one time
lines = r.iter_lines()

# for line in lines:
#     print line

# another way to do it
first_line = next(lines)
print first_line
