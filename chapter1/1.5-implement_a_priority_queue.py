import heapq


class PriorityQueue(object):
    """docstring for PriorityQueue"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
