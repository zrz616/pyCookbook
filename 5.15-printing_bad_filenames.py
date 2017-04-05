import os


def bad_filename(filename):
    # repr(filename)[0:-1] output: "'filename'"
    # repr(filename)[1:-1] output: "filename"
    return repr(filename)[1:-1]


# filename = "b\udce4d.txt"
for filename in os.listdir('.'):
    try:
        print(filename)
    except UnicodeEncodeError as e:
        print('bad')
        print(bad_filename(filename))
