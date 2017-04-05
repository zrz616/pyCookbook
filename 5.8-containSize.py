from functools import partial


RECORD_SIZE = 32

with open('abcc.txt', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
