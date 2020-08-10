class Element:
    def __init__(self,value):
        self.value = value
        self.next = None

class List:
    def __init__(self,head=None):
        self.head = head
        self.len = 1
    
    def append(self,element):
        current = self.head
        if self.head == None:    
            self.head = element
        
        else:
            while current.next:
                current = current.next
            current.next = element
        self.len += 1

    def print_list(self):
        current = self.head
        if current == None:
            print('No elements yet')
        else:
            while current.next:
                print(current.value)
                current = current.next
            print(current.value)

    def get_pos(self,position):
        counter = 1
        current = self.head
        while current.next:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self,element,position):
        current = self.head
        pos = 1
        if position < 1:
            print('Not a valid position!!!')
            return None
        if position > self.len:
            print('Index Out of Bounds!!!')
            return None
        
        while current.next:
            if pos == position:
                element.next = current.next
                current.next = element
                print('Element Inserted')
                return
            current = current.next
            pos += 1
        if pos == self.len:
            current.next = element

    def delete_elem(self,element):
        current = self.head
        while current.next:
            if element == current.next.value:
                current.next = current.next.next
                current.next.next = None
            current = current.next

    def delete_pos(self,position):
        current = self.head
        if position > self.len:
            print('Out of Bounds!!')
            return
        if position < 1:
            print('Invalid Position!!')
            return
        for i in range(position-1):
            current = current.next
        current.next = current.next.next
        current.next.next = None
        

e1 = Element(43)
e2 = Element(12)
e3 = Element(56)

l1 = List(e1)
l1.append(e2)
l1.insert(e3,2)

l1.print_list()