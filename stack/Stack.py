from Item import Item

class Stack:

    def __init__(self):

        self.head = None

    def __repr__(self):
        return self.head
    
    def set_head(self, head):
        self.head = head
    
    def get_head(self):
        return self.head
    
    def is_empty(self):
        
        if(self.get_head == None):
            return True
        
        return False
    
    def push(self, value):

        item = Item(value)

        item.set_before(self.head)

        self.set_head(item)

    def pop(self):
        
        if(self.is_empty):
            raise Exception("Stack Empty")
        
        old_head = self.get_head()

        self.head = self.head.before()

        return old_head
    
    def __repr__(self):
        return str(self.get_head())


    

        
