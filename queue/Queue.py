from Node import Node

class Queue:

    def __init__(self):

        self.head = None
        self.tail = None

    def __repr__(self):
        return str(self.head)
    
    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail
    
    def set_tail(self, value):
        self.tail = value

    def set_head(self, value):
        self.head = value
    
    def is_empty(self):
        return self.head is None


    def enqueue(self, value):

        node = Node(value)

        if self.tail is None:
            self.set_head(node)
            self.set_tail(node)
                    
        else:
            self.tail.set_next(node)
            self.tail = node

    def dequeue(self):

        if self.is_empty():
            raise Exception("Empty List")
        
        removed_item = self.head

        self.head = removed_item.get_next()

        if self.head is None:
            self.tail = None
        
        return removed_item


