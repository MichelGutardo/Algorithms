#!/bin/python3

#Queue implementation using list
#Just use append() to push and remove with pop(0) elements in FiFo order

# List is a Python's built-in data structure, but is quite slow because the shifting all elements by on
# requiring O(n) 

queue = [] 


# append() to push element in the queue

queue.append("M")
queue.append("i")
queue.append("c")
queue.append("h")
queue.append("e")
queue.append("l")


print("Initial queue")
print(queue)

# Removing elements 
print ("\nPop element from queue:")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print ("\nQueue after removing elements:")
print(queue)




