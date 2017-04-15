# re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
# re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
# re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
# re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

import re

text1 = '/* this is a comment */'
text2 = """/* this is a
 multiline comment */"""
comment = re.compile(r'/\*(.*?)\*/')
print(comment.findall(text1))
print(comment.findall(text2))
comment = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)
print(comment.findall(text2))
comment = re.compile(r'/\*((?:.|\n).*?)\*/', flags=re.DOTALL)
print(comment.findall(text2))
