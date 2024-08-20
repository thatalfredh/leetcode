from sortedcontainers import SortedSet

class StockPrice:

    def __init__(self):
        self.records = {}
        self.sorted_set = SortedSet()
        self.curr_time = 0
        self.max_price = 0
        self.min_price = float('inf')
        
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.records.keys():
            self.sorted_set.remove((self.records[timestamp], timestamp))
        self.curr_time = max(self.curr_time, timestamp)
        self.records[timestamp] = price
        self.sorted_set.add((price, timestamp))

    def current(self) -> int:
        return self.records[self.curr_time]

    def maximum(self) -> int:
        return self.sorted_set[-1][0]
        
    def minimum(self) -> int:
        return self.sorted_set[0][0]
        
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

