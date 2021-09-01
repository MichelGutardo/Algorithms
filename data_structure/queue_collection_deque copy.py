#!/bin/python3

#collection_deque implementation using collection.deque class
#Use put() to add and get() remove elements in FiFo order
#Use empty() to check if queue is empty 
#Use full() to check if queue is full with size limit
from queue import Queue
import queue

queue_queue = Queue(maxsize=6)

# put() to push element in the collection_deque



print("Check if queue os full:")
print(queue_queue.full())


queue_queue.put("M")
queue_queue.put("i")
queue_queue.put("c")
queue_queue.put("h")
queue_queue.put("e")
queue_queue.put("l")


print("Initial queue_queue:")
print(queue_queue.queue)

# Removing elements 
print("\nPop element from queue_queue:")
print(queue_queue.get())
print(queue_queue.get())
print(queue_queue.get())
print(queue_queue.get())
print(queue_queue.get())
print(queue_queue.get())

print ("\nqueue_queue after removing elements is empty?:")
print(queue_queue.empty())




