""" 
Code: Stack Implementation using list inheritance (LIFO)

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

class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            return "Stack is Empty"

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            return "Stack is Empty"

    @property
    def size(self):
        return len(self)

    # Block the functions
    def insert(self, index, value):
        return "Invalid Operation"
    
    def remove(self, value):
        return "Invalid Operation"

    def clear(self):
        return "Invalid Operation"

    def extends(self, items):
        return "Invalid Operation"

    def __setitem__(self, key, value):
        print("Invalid Operation")

    def __delitem__(self, key):
        print("Invalid Operation")

s1 = Stack()
print(s1.is_empty())

s1.push(23)
s1.push(678)
s1.push(89)
s1.push(178)

print('Pop: ', s1.pop())
print('Peek: ', s1.peek())
print('Size: ', s1.size)

print(s1.extends([12,3]))
s1[0] = 100
del s1[1]