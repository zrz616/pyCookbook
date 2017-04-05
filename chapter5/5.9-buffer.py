import os.path

record_size = 32


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


def read_into_buffer_block(filename):
    buf = bytearray(record_size)
    with open('abc1.txt', 'rb') as f:
        while True:
            n = f.readinto(buf)
            if n < record_size:
                break


if __name__ == '__main__':

    with open('abc.txt', 'wb') as f:
        f.write(b'Hello World')
    buf = read_into_buffer('abc.txt')
    buf[0:5] = b'Hallo'
    print(buf, buf[0:5])

    with open('newabc.txt', 'wb') as f:
        f.write(buf)
