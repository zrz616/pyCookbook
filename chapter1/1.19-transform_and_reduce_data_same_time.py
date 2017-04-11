import os

nums = [1, 2, 3, 4, 5]
print(sum(x * x for x in nums))
# 当前目录有以是否有以.py结尾的文件
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python!')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

s = sum(x * x for x in nums)
s = sum([x * x for x in nums])
