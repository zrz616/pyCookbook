s = ' hello world \n'
print(s.strip())
print(s.lstrip(), s.rstrip())

t = '-----hello====='
print(s.strip(('-=')))

with open('card.txt', 'rt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
