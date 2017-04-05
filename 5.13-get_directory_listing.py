import os
import glob
import fnmatch


path = 'c:/Users/xx/cookbook/'

# 返回目录下的所有文件列表
names = os.listdir(path)
print(names)

# 返回所有文件
names = [name for name in os.listdir(path)
         if os.path.isfile(os.path.join(path, name))]
print(names)

# 返回所有目录
dirnames = [name for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))]
print(dirnames)

# 返回.py文件
pyfiles = [name for name in os.listdir(path)
           if name.endswith('.py')]
print(pyfiles)

# 文件名匹配
pyfiles = glob.glob(os.path.join(path, '*.py'))
print(pyfiles)

pyfiles = [name for name in os.listdir(path)
           if fnmatch.fnmatch(name, '*.py')]

pyfiles = glob.glob('*.py')

name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)

file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
