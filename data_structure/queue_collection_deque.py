#!/bin/python3

#collection_deque implementation using collection.deque class
#Use append() to add and popleft() elements in LIFO order

# Deque if preferred over list because append is quicker [ O(1) ], but 
# pop operations as compared to list [ O(n) ] 

from collections import deque

collection_deque = deque()

# append() to push element in the collection_deque

collection_deque.append("M")
collection_deque.append("i")
collection_deque.append("c")
collection_deque.append("h")
collection_deque.append("e")
collection_deque.append("l")

print("Initial collection_deque")
print(collection_deque)

# Removing elements 
print("\nPop element from collection_deque:")
print(collection_deque.popleft())
print(collection_deque.popleft())
print(collection_deque.popleft())
print(collection_deque.popleft())
print(collection_deque.popleft())
print(collection_deque.popleft())

print ("\ncollection_deque after removing elements:")
print(collection_deque)




