# Using list
stock_price = []

stock_price.insert(0, 111.0)  # will be pushed by the next line
stock_price.insert(0, 333.0)  # will be pushed by the next line
stock_price.insert(0, 444.0)  # will be the first one

# print(stock_price)

stock_price.pop()  # Implementing pop() will create FIFO
# print(stock_price)

# Using dequeue
from collections import deque

que = deque()
# TO create FIFO, use appendleft
# que.appendleft(5)
# que.appendleft(7)
# que.appendleft(10)
# print(que)


# create Class
class MyQueue:
    def __init__(self):
        self.buffer = deque()

    def enquque(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


# TEST CLASS
# justq = MyQueue()
# justq.enquque({"Info": "Stock Price", "Skill": "Australia", "Price": 22.21})
# justq.enquque({"Info": "Stock Price", "Skill": "Eldia", "Price": 21.42})
# justq.enquque({"Info": "Stock Price", "Skill": "Eldia", "Price": 12.42})

# # will get the information one by one (queueing by the information)
# print(justq.dequeue())
# print(justq.dequeue())
# print(justq.dequeue())

# print(justq.is_empty())
# print(justq.size())
# print(justq.buffer)

# EXERSICE
# pre-requisite: multithreading: utilizinig idle time
import time

food_q = MyQueue()


def place_order(food_list):
    for food in food_list:
        food_q.enquque(food)
        print(f"{food} is added into queue...")
        time.sleep(0.5)  # DELAY A


def serve_order():
    time.sleep(1)  # DELAY B
    # for _ in range(len(food_q.buffer)):
    while True:
        order = food_q.dequeue()
        print(f"{order} is dequeue...")
        time.sleep(2)  # DELAY C
        if food_q.is_empty():
            print("Order is finished!")
            break


"""
NOTE : Understanding the Delay part in Laymen

1. 1st and 2nd foods ordered took 1 s. 
2. While waiting the 1 sec from `place order()` finish, 1 s has been consumed in `served_order()` at the same time.
3. As 1 s finished, the thread is moved to p2; dequeue the food, 
then waiting for 2 seconds. While waiting the 2 seconds finished, 
`place_order()` utilized the time to place more order. 
4. New orders is placed until 1 sec is passed, moving the task to `serve_order()`. 
5. The iteration continue. 

"""

import threading

food_order = ["pizza", "macaroni", "soup", "nasi goreng", "coke"]
p1 = threading.Thread(target=place_order, args=(food_order,))
p2 = threading.Thread(
    target=serve_order,
)

p1.start()
p2.start()

p1.join()
p2.join()
