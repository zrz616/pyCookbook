import re

num = re.compile('\d+')
print(num.match('123').group())
print(num.match('\u0661\u0662\u0663').group())
