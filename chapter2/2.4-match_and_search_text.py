import re

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

pattern_date = re.compile(r'\d+/\d+/\d+')

# 从头开始匹配，未匹配到返回NoneType
if pattern_date.match(text1):
    print('yes')
else:
    print('no')

if pattern_date.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# 匹配整个字符串，匹配到第一就返回匹配对象
m = pattern_date.search(text)
print(m.group())

# +会把捕获到的最后一个放入捕获组中
pattern_date = re.compile(r'(..)+')
m = pattern_date.match('a1b2c3')
print(m.group())
print(m.groups())

pattern_date = re.compile(r'(\d+)/(\d+)/(\d+)')
m = pattern_date.match('11/27/2012')
# group(0)是历史匹配项与捕获组无关，
# groups()是所有捕获组
print(m.group(0), m.group(1), m.group(2), m.group(3))
print(m.groups())

# 匹配整个字符串全部匹配
for month, day, year in pattern_date.findall(text):
    print('{}-{}-{}'.format(year, day, month))

for m in pattern_date.finditer(text):
    print('{}-{}-{}'.format(*m.groups()))
