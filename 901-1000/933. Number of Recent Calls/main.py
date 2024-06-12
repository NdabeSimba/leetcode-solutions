from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)


self = RecentCounter()
print(RecentCounter.ping(self, 1))
print(RecentCounter.ping(self, 100))
print(RecentCounter.ping(self, 3001))
print(RecentCounter.ping(self, 3002))
