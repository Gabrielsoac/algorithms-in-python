class NaryNode:

    def __init__(self, value):

        self.value = value
        self.children = []

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def get_children(self):
        return self.children
    
    def insert_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return str(self.value)
