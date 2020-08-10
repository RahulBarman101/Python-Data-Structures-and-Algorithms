class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class btree:
    def __init__(self):
        self.height = 0
        self.nodes = 0
        self.root = None

    def insert(self,value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            run = True
            current = self.root
            while run:
                
                if node.value < current.value:
                    if current.left is None:
                        current.left = node
                        run = False
                        self.nodes += 1
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        run = False
                        self.nodes += 1
                        break
                    else:
                        current = current.right

    def print_tree(self):
        current = self.root
        print(current.value)
        while current.left or current.right:
            # print(current.value)
            if current.left:
                current_p = current
                current = current.left
                print(current.value)
            elif current.right:
                current_p = current
                current = current.right

    def print_tree(self,current):
        if current:
            print(current.value)
            self.print_tree(current.left)
            self.print_tree(current.right)

    def get_height(self,node):
        if node is None:
            return 0
        else:
            
            ld = self.get_height(node.left)
            rd = self.get_height(node.right)

            if ld > rd:
                return ld+1
            else:
                return rd+1

    def search(self,value):
        current = self.root
        while True:
            if value == current.value:
                print('Node Found!!')
                break
            elif value < current.value:
                current = current.left
                if current.left is None:
                    print('Node is not present.....')
                    break
            else:
                current = current.right
                if current.right is None:
                    print('Node is not present.....')
                    break


root = btree()
root.insert(10)
root.insert(8)
root.insert(4)
root.insert(9)
root.insert(12)
root.insert(11)
root.insert(17)
root.search(15)
root.print_tree(root.root)
print(root.get_height(root.root))