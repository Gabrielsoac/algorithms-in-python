from NaryTree import NaryTree

my_tree = NaryTree()

my_tree.set_root(10)

print(my_tree.get_root())

my_tree.insert(my_tree.get_root(), 12)
my_tree.insert(my_tree.get_root(), 14)
my_tree.insert(my_tree.get_root(), 15)

my_tree.pre_order_transversal(my_tree.get_root())

my_node = my_tree.find_node(my_tree.get_root(), 14)

my_tree.insert(my_node, 444)

print(" ")

my_tree.pre_order_transversal(my_tree.get_root())


