import io


s = io.StringIO()
s.write('Hello World\n')
print('This is a test', file=s)
print(s.getvalue())

s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
