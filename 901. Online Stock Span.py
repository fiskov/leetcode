# 901. Online Stock Span
# https://leetcode.com/problems/online-stock-span/

import time


class StockSpanner:
    def __init__(self):
        self.days_stock = []
        self.span = 1
        pass

    def next(self, price: int) -> int:
        if len(self.days_stock):
            if self.days_stock[-1][0] == price:
                self.days_stock[-1][1] += 1
                self.span += 1
            else:
                if self.days_stock[-1][0] > price:
                    self.days_stock.append([price, 1])
                    self.span = 1
                else:
                    self.span = 1
                    pos = len(self.days_stock) - 1
                    while pos >= 0 and self.days_stock[pos][0] <= price:
                        self.span += self.days_stock[pos][1]
                        pos -= 1
                    self.days_stock[-1][0] = price
                    self.days_stock[-1][1] += 1
        else:
            self.days_stock.append([price, 1])

        return self.span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


start = time.time()

stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # return 1
print(stockSpanner.next(80))  # return 1
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(70))  # return 2
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(75))  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(stockSpanner.next(85))  # return 6

print("--")
stockSpanner = StockSpanner()
print(stockSpanner.next(29))  # return 1
print(stockSpanner.next(91))  # return 2
print(stockSpanner.next(62))  # return 1
print(stockSpanner.next(76))  # return 2
print(stockSpanner.next(51))  # return 1

print("--")
stockSpanner = StockSpanner()
maxvalue = 5000
for i in range(1, maxvalue):
    stockSpanner.next(i)
print(stockSpanner.next(maxvalue))
print("time = ", time.time() - start)
