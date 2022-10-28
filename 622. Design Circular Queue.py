# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
from typing import List


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.data = [0]*self.capacity
        self.head_pos = -1
        self.tail_pos = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size < self.capacity:
            self.size += 1
            self.head_pos += 1
            if self.head_pos >= self.capacity:
                self.head_pos = 0
            self.data[self.head_pos] = value
            return True
        return False

    def deQueue(self) -> bool:
        if self.size:
            self.size -= 1
            self.tail_pos += 1
            if self.tail_pos >= self.capacity:
                self.tail_pos = 0
            return True
        return False

    def Front(self) -> int:
        if self.size:
            return self.data[self.tail_pos]
        return -1

    def Rear(self) -> int:
        if self.size:
            return self.data[self.head_pos]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # return True
print(myCircularQueue.enQueue(2))  # return True
print(myCircularQueue.enQueue(3))  # return True
print(myCircularQueue.enQueue(4))  # return False
print(myCircularQueue.Rear()    )      # return 3
print(myCircularQueue.isFull()  )    # return True
print(myCircularQueue.deQueue() )   # return True
print(myCircularQueue.enQueue(4))  # return True
print(myCircularQueue.Rear()    )      # return 4