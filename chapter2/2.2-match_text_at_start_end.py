import os

filename = '.txt'
filename.endswith('.txt')
filename.startswith('file:')

filenames = os.listdir('.')
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))
