from Graph import *

g = Graph()
g.add_arrow("A1", "B1")
g.add_arrow("A1", "C1")
g.add_arrow("B1", "D1")
g.add_arrow("C1", "D1")

## g.show_graph()

g.depth_first_search("A1")

