import sys
import os

# 系统默认文件明编码解码方式
sys.getfilesystemencoding()

# 使用系统默认编码方式解码
os.listdir('.')

# windows已抛弃
os.listdir(b'.')
