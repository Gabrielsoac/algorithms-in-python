class Graph:

    def __init__(self):

        self.graph = {}
    
    def add_node(self, node):

        if node not in self.graph:

            self.graph[node] = []

    def add_arrow(self, node_one, node_two):

        self.add_node(node_one)
        self.add_node(node_two)
        self.graph[node_one].append(node_two)
        self.graph[node_two].append(node_one)
    
    def show_graph(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")

    def depth_first_search(self, node, visiteds=None):

        if visiteds == None:
            visiteds = set()

        visiteds.add(node)
        print(node, end=' ')

        for adjacent_node in self.graph[node]:
            if adjacent_node not in visiteds:
                self.depth_first_search(adjacent_node, visiteds)