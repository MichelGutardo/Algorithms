#!/bin/python3

from queue import Queue

queue_queue = Queue(maxsize=6)


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




