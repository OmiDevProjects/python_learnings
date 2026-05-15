""" 
Code: Singly Linked List
Description: 

"""

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, value):
        node = Node(item=value)
        if not self.is_empty():
            node.next = self.start
        self.start = node

    def insert_at_last(self, value):
        node = Node(item=value)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def insert_at(self, data, value):
        node = Node(item=data)
        if not self.is_empty():
            temp = self.search_item(value)
            if temp:
                node.next = temp.next
                temp.next = node
    
    def show(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=', ')
                temp = temp.next
            print()

    def search_item(self, value):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == value:
                    return temp
                temp = temp.next

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == None:
                self.start == None
            else:
                self.start = self.start.next
            
    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def delete_item(self, value):
        if not self.is_empty():
            if self.start.item == value:
                self.start = self.start.next
            else:
                temp = self.start
                while temp is not None:
                    if temp.next.item == value:
                        temp.next = temp.next.next
                    temp = temp.next



s1 = SLL()
s1.insert_at_first(23)
s1.insert_at_last(40)
s1.insert_at_first(30)
s1.insert_at_last(46)
s1.show()
# print(s1.search_item(23).item)

print('Inserting element at')
s1.insert_at(34, 46)
s1.show()

# print('Deleting First Element')
# s1.delete_first()
# s1.show()

# print('Deleting Last Element')
# s1.delete_last()
# s1.show()

# print('Deleting Element for Linkedlist')
# s1.delete_item(30)
# s1.show()