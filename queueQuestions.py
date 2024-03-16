#https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md

from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        if len(self.buffer) == 0:
            print( "Queue is Empty")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]
    
food_ordering_queue = Queue()

def order_placed(orders):
    for order in orders:
        print("order placed for : ", order)
        food_ordering_queue.enqueue(order)
        time.sleep(0.5)

def order_served():
    time.sleep(1)
    while True:
        order = food_ordering_queue.dequeue()
        print("order Served For : ", order)
        time.sleep(2)

def binary_numbers(n):
    b_queue = Queue()
    b_queue.enqueue("1")

    for i in range(n):
        front = b_queue.front()

        print(" ",front)
        b_queue.enqueue(front + "0")
        b_queue.enqueue(front + "1")

        b_queue.dequeue()



if __name__=='__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=order_placed, args=(orders,))
    t2 = threading.Thread(target=order_served)

    t1.start()
    t2.start()
    binary_numbers(10)