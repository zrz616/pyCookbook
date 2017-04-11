record = ''.join(list(str(x) for x in range(0, 100)))
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

a = slice(5, 50, 2)
print(a.start, a.stop, a.step)

s = "HelloWorld"
# 用indices指定序列的长度，来计算start、stop
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])
