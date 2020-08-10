class Element:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,head=None):
        self.head = head
        self.len = 1

    def push(self,value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Element(value)
        self.len += 1

    def pop(self):
        current = self.head
        for i in range(self.len-2):
            current = current.next
        current.next = None
    
    def print_list(self):
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

e1 = Element(21)    
stack = Stack(e1)
stack.push(45)
stack.push(65)
stack.print_list()
stack.pop()
print()
print()
stack.print_list()