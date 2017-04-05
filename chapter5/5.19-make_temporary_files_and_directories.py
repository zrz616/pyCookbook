from tempfile import TemporaryFile


with TemporaryFile('w+t') as f:
    f.write('Hello world\n')
    f.write('Testing\n')

    f.seek(0)
    data = f.read()
    print(data)


# with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
