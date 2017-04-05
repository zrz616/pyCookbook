import os


path = 'C:/Users/xx/cookbook'
print(os.path.basename(path))
print(os.path.dirname(path))
join_dir = os.path.join('tmp', 'data', os.path.basename(path))
print(join_dir)
path = '~/cookbook/5.6-stringIO.py'
print(os.path.expanduser(path))
split_dir = os.path.splitext(path)
print(split_dir)
