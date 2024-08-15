from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def __repr__(self):

        return str(self.head)
    
    def size(self):

        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.get_next()
    
        return count
    
    def search(self, data):

        current = self.head

        while current != None:
            
            if current.get_data() == data:
                return True
            
            current = current.get_next()

        return False
    
    def remove(self, data):
        
        current = self.head
        previous = None
        found = False

        while not found:

            if current.get_data() == data:
                found = True
            
            else:
                previous = current
                current = current.get_next()       

        if current == None:
            raise ValueError("Not Found")

        if previous == None:
            self.head = current.get_next()
        
        else:
            previous.set_next(current.get_next())
        

        
