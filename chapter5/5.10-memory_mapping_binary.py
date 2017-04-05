# os.O_RDONLY: 以只读的方式打开
# os.O_WRONLY: 以只写的方式打开
# os.O_RDWR : 以读写的方式打开
# os.O_APPEND: 以追加的方式打开
# os.O_CREAT: 创建并打开一个新文件
# os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
# os.O_EXCL: 如果指定的文件存在，返回错误
# 仅unix有效
# os.O_NONBLOCK: 打开时不阻塞（）
# os.O_SHLOCK: 自动获取共享锁
# os.O_EXLOCK: 自动获取独立锁
# GNU扩展
# os.O_DIRECT: 消除或减少缓存效果
# os.O_FSYNC : 同步写入
# os.O_NOFOLLOW: 不追踪软链接

import os
import mmap


# mmap.ACCESS_READ 只读
# mmap.ACCESS_WRITE 写
# mmap.ACCESS_COPY 拷贝访问
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


if __name__ == '__main__':
    size = 10000
    with open('data', 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x01')

    m = memory_map('data')
    print(len(m))

    # 支持切片操作
    m[0:11] = b'Hello World'
    print(m[0:11])
    m.close()

    with open('data', 'rb') as f:
        print(f.read(11))

    # mmap对象支持上下文管理器
    with memory_map('data') as m:
        print(m.read(11))

    # 可用memoryview解析
    m = memory_map('data')
    v = memoryview(m).cast('I')
    v[0] = 7
    print(m[0:4])
    m[0:4] = b'\x07\x01\x00\x00'
    print(v[0])
