from win_unicode_console import streams
import sys


# windows下要设置这条
streams.stdout_text_transcoded.buffer = streams.stdout_text_str
sys.stdout.buffer.write(b'hello')
