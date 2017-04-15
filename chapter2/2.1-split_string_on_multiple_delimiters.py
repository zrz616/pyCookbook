import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*', line)

fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values, delimiters)
''.join(v + d for v, d in zip(values, delimiters))
fields = re.split(r'(?:;|,|\s)\s*', line)
print(fields)
