from collections import OrderedDict
import json


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# 对于一个已经存在的键的重复赋值不会改变键的顺序。
d['foo'] = 5
for key in d:
    print(key, '\b=', d[key])

print(json.dumps(d))
