class Item:

    def __init__(self, value=None, before=None):

        self.value = value
        self.before = before

    def __repr__(self):
        return str(self.value) + "\n" + str(self.before)
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def set_before(self, before):
        self.before = before

    def get_before(self):
        return self.before