import os


fd = os.open('date', os.O_WRONLY, os.O_CREAT)
f = open(fd, 'wt')
f.write('2017/4/2')
f.close()

fd = os.open('date', os.O_WRONLY, os.O_CREAT)
# Create a file object, but don't close underlying fd when done
f = open(fd, 'wt', closefd=False)
f.write('2017/4/2')
f.close()
