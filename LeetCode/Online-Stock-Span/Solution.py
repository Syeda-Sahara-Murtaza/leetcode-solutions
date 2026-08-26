1class StockSpanner:
2    def __init__(self):
3        self.stack = []
4        self.index = -1
5    def next(self, price: int) -> int:
6        self.index += 1
7        while self.stack and self.stack[-1][0] <= price:
8            self.stack.pop()
9        if not self.stack:
10            span = self.index + 1
11        else:
12            span = self.index - self.stack[-1][1]
13        self.stack.append((price,self.index))
14        return span
15
16
17
18# Your StockSpanner object will be instantiated and called as such:
19# obj = StockSpanner()
20# param_1 = obj.next(price)