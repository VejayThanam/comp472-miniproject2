import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, state):
        heapq.heappush(self.queue, (priority, state))

    def empty(self):
        return len(self.queue) == 0

    def pop(self):
        return heapq.heappop(self.queue)