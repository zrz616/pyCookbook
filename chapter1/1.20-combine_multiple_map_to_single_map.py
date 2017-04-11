from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c)
print(dict(zip(c.keys(), c.values())))

c['z'], c['w'] = 2, 40
del c['x']
print(a)
# try:
#     del c['y']
# except KeyError:
#     print('not find this key')
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
values = values.parents
print(values)
values = values.parents
print(values)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)
