""" 
Code: Stack Implementation using list (LIFO)

Description:
    Implemented a Stack data structure using Python lists
    to perform standard stack operations.

Features:
    - Push elements onto the stack
    - Pop elements from the stack
    - Peek the top element
    - Check stack size
    - Check whether the stack is empty

Concepts Used:
    - Object-Oriented Programming (OOP)
    - List operations
    - LIFO (Last In First Out) principle

Purpose:
    This project demonstrates the implementation and working
    of a Stack data structure using Python's built-in list.


| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |
| is_empty  | O(1)            |
| Size      | O(1)            |

"""

class Stack:
    def __init__(self):
        self.lst = []

    def is_empty(self):
        return len(self.lst) == 0

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return "Stack is Empty"

    @property
    def size(self):
        return len(self.lst)
    
    def peek(self):
        if not self.is_empty():
            return self.lst[-1]
        else:
            return "Stack is Empty"

s1 = Stack()
print('Is Empty: ', s1.is_empty())
s1.push(23)
print('Is Empty: ', s1.is_empty())

s1.push(45)
s1.push(16)
s1.push(276)
s1.push(73)

print('Pop: ', s1.pop())
print('Peeking: ', s1.peek())
print('Size: ', s1.size)