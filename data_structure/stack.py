#!/bin/python3

#Stack implementation using list
#Just use append() to push and remove with pop() elements in LIFO order
stack = [] 


# append() to push elementn in the stack

stack.append("M")
stack.append("i")
stack.append("c")
stack.append("h")
stack.append("e")
stack.append("l")


print("Initial stack")
print(stack)

# pop() element in LIFO order
print ("\nPop element from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print ("\nStack after pop elements:")
print(stack)




