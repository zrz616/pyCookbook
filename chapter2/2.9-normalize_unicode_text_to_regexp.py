import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1 == s2)

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))

t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print(t1 == t2)
print(ascii(t1))

t1 = unicodedata.normalize('NFD', s1)
print(''.join(i for i in t1 if not unicodedata.combining(i)))
