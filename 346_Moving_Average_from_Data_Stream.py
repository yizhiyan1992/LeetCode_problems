#use a deque
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size=size
        self.DQ=deque([])

    def next(self, val: int) -> float:
        if len(self.DQ)==self.size:
            self.DQ.popleft()
        self.DQ.append(val)
        return sum(self.DQ)/len(self.DQ)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
