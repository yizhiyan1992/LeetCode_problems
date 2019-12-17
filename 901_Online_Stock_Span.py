# Mono stack
# Time complexity: O(n)
class StockSpanner:

    def __init__(self):
        self.stack=[]
        # RES stack records the maximum consecutive days with lower or equal price for ith day.
        self.RES=[]
    def next(self, price: int) -> int:
        res=1
        while self.stack and self.stack[-1]<=price:
            self.stack.pop()
            res=res+self.RES.pop()
        self.stack.append(price)
        self.RES.append(res)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
