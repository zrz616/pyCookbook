from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
words_count = Counter(words)
top_three = words_count.most_common(3)
print(top_three)
print(words_count['look'])
print(words_count['not'])

# 手动统计
more_word = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in more_word:
    words_count[word] += 1
words_count.update(more_word)
a = Counter(words)
b = Counter(more_word)
c = a + b
print(c)
