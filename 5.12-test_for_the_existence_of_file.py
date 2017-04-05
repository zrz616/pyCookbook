import os.path
import time

path = 'c:/Users/xx/cookbook/'
file_path = os.path.join(path, "abc.txt")
link_path = os.path.join(path, "abc.txt.link")
# 判断路径是否存在
print(os.path.exists(path))
print(os.path.exists('c:/Users/xxx/coookbook/'))

# 判断路径是否为目录
print(os.path.isdir(path))

# 判断路径是否为文件
print(os.path.isfile(file_path))

# 判读路径是否为link（linux的链接）
print(os.path.islink(link_path))

# 获取路径真实地址
print(os.path.realpath(link_path))

# 获得文件大小
print(os.path.getsize(file_path))

# 获得文件修改日期
# getmtime 最后修改时间
# getatime 最后访问时间
# getctime 元数据改变时间
print(time.ctime(os.path.getmtime(file_path)))
print(time.ctime(os.path.getatime(file_path)))
print(time.ctime(os.path.getctime(file_path)))
