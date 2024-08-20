from NaryNode import NaryNode

class NaryTree:

    def __init__(self):

        self.root = None

    def set_root(self, value):
        self.root = NaryNode(value)

    def get_root(self):
        return self.root

    def insert(self, parent, value):

        if parent:

            new_node = NaryNode(value)

            parent.insert_child(new_node)
    
    def pre_order_transversal(self, node):

        if node:

            print(node.value, end=' ')
            for child in node.children:
                self.pre_order_transversal(child)

    def find_node(self, node, target_value):

        if node is None:
            return None
        
        if node.get_value() == target_value:
            return node
        
        for child in node.get_children():
            
            result = self.find_node(child, target_value)

            if result is not None:
                return result
        
        return None
