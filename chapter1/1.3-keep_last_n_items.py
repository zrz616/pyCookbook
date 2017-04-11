# 在队列两端插入或删除元素时间复杂度都是 O(1) ，
# 而在列表的开头插入或删除元素的时间复杂度为 O(N) 。
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('card.txt', 'rt') as f:
        for line, pre_line in search(f, 'python'):
            for line in pre_line:
                print(line, end="")
            print(line, end="")
            print('-' * 20)
